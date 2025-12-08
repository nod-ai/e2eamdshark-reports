from functools import reduce
from pathlib import Path
import xlsxwriter
import argparse
from collections import defaultdict
import re


class TestInfo:
    def __init__(self, name, status):
        self._name = name
        self._pass_status = status

    @property
    def name(self):
        return self._name

    @property
    def is_pass(self):
        if self._pass_status == "PASS":
            return 1
        return 0

    @property
    def stage(self):
        if self._pass_status != "PASS":
            return self._pass_status
        return ""


def create_summary(report_dir, output_file, report_file_list, test_run_dir):

    workbook = xlsxwriter.Workbook(output_file)
    worksheet_summary = workbook.add_worksheet("Summary")

    worksheet_summary.write("B3", "Index")
    worksheet_summary.write("C3", "Test File")
    worksheet_summary.write("D3", "Total Count")
    worksheet_summary.write("E3", "Pass")

    # report_directory_name = "./reports"
    md_file_count = 3
    print(f"Report directory: {report_dir}")
    print(f"Test run directory: {test_run_dir}")
    md_file_list = []
    if report_file_list is not None:
        with open(report_file_list) as f:
            for line in f.readlines():
                md_file_list.append(report_dir / Path(line.strip()))

    else:
        md_file_list = report_dir.glob("*.md")

    reason_map = defaultdict(lambda: defaultdict(list))

    for md_file in md_file_list:
        print(f"Processing {md_file}")
        test_info_list = []
        md_file_count += 1

        worksheet_md = workbook.add_worksheet(f"{Path(md_file).stem}")

        with open(md_file) as f:
            marker_seen = False
            test_data_details = 0
            for line in f.readlines():
                if line.startswith("## Test Run Detail"):
                    marker_seen = True

                if marker_seen:
                    if test_data_details == 1:
                        test_data_details = 2
                        continue

                    if line.startswith(
                        "| Test | Exit Status | Mean Benchmark Time (ms) | Notes |"
                    ):
                        test_data_details = 1

                    if test_data_details == 2:
                        line_arr = line.strip().split("|")
                        test_info_list.append(
                            TestInfo(line_arr[1].strip(), line_arr[2].strip())
                        )

        total_count = len(test_info_list)
        pass_count = reduce(
            lambda acc, test: acc + 1 if test.is_pass else acc, test_info_list, 0
        )

        worksheet_summary.write(f"B{md_file_count}", md_file_count - 3)
        worksheet_summary.write(f"C{md_file_count}", f"{md_file.name}")
        worksheet_summary.write(f"D{md_file_count}", total_count)
        worksheet_summary.write(f"E{md_file_count}", pass_count)

        # print("-------------------------")
        # print(f"{md_file.name}, {total_count}, {pass_count}")
        # print("-------------------------")

        worksheet_md.write("C2", f"{md_file.name}")
        worksheet_md.write("C3", "Test Name")
        worksheet_md.write("D3", "Status")
        worksheet_md.write("E3", "Fail Stage")
        worksheet_md.write("F3", "Fail Reason")
        test_count = 3

        for t in test_info_list:
            test_count += 1

            worksheet_md.write(f"C{test_count}", f"{t.name}")
            if t.is_pass:
                worksheet_md.write(f"D{test_count}", "PASS")
            else:
                # print(f",{t.name}, FAIL, {t.stage}")
                worksheet_md.write(f"D{test_count}", "FAIL")
                worksheet_md.write(f"E{test_count}", f"{t.stage}")
                stage_file = test_run_dir / Path(f"{t.name}/{t.stage}.log")
                try:
                    with open(stage_file) as f:
                        line_arr = f.readlines()
                        reason = line_arr[-1]
                        reason_extra = ""
                        # print(f"Reason1: {reason}")
                        if reason.startswith("iree-run-module") or reason.startswith(
                            "iree-compile"
                        ):
                            reason = line_arr[-2]
                            reason_extra = line_arr[-1]
                            reason_key = ""
                            # print(f"Reason2: {reason} {reason_extra}")
                            try:
                                detail_file = (
                                    test_run_dir
                                    / Path(f"{t.name}")
                                    / "detail"
                                    / f"{t.stage}.detail.log"
                                )
                                with open(detail_file) as f:
                                    for line in f.readlines():
                                        if "error:" in line:
                                            reason_extra += ":" + line.strip()
                                            reason_key = (
                                                line.split("error:")[-1]
                                                .split(":")[0]
                                                .strip()
                                            )
                                            reason_key = reason_key.split(";")[0]
                                            reason_key = re.sub(
                                                r"'[^']*'", "'OP'", reason_key
                                            )
                                            break
                            except Exception as e:
                                print(f"Error reading {detail_file}: {e}")
                                pass
                        else:
                            reason_key = reason.split(":")[0]
                        # print(f"Reason3: {reason_key}")
                        # print(f"Reason4: {reason_extra}")
                        reason_map[t.stage][reason_key].append(t.name)
                    worksheet_md.write(f"F{test_count}", f"{reason}")
                    worksheet_md.write(f"G{test_count}", f"{reason_extra}")
                except Exception as e:
                    print(f"Error reading {stage_file}: {e}")
                    pass
        worksheet_md.autofilter(f"C3:G{test_count}")
    worksheet_reason_summary = workbook.add_worksheet("Reason_Histogram")
    reason_key_count = 3
    worksheet_reason_summary.write("A3", "Stage")
    worksheet_reason_summary.write("B3", "Reason")
    worksheet_reason_summary.write("C3", "Count")
    for stage, reason_key_map in reason_map.items():
        for reason_key, test_name_list in reason_key_map.items():
            reason_key_count += 1
            worksheet_reason_summary.write(f"A{reason_key_count}", stage)
            worksheet_reason_summary.write(f"B{reason_key_count}", reason_key)
            worksheet_reason_summary.write(f"C{reason_key_count}", len(test_name_list))
    worksheet_reason_summary.autofilter(f"A3:C{reason_key_count}")
    workbook.close()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--report-dir", type=Path, default=Path("./reports"))
    parser.add_argument("-l", "--report-file-list", type=Path, default=None)
    parser.add_argument("-t", "--test-run-dir", type=Path, default=Path("./test-run"))
    parser.add_argument("-o", "--output-file", type=str, default="summary.xlsx")
    args = parser.parse_args()

    report_dir = args.report_dir
    output_file = args.output_file
    file_list = args.report_file_list
    test_run_dir = args.test_run_dir

    create_summary(report_dir, output_file, file_list, test_run_dir)


if __name__ == "__main__":
    main()
