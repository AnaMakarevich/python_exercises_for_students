class ReportGenerator:
    def generate_report(self, data):
        print(f"Generating report for {data}")


class ReportSaver:
    @staticmethod
    def save_to_file(data):
        with open("report.txt", "w") as file:
            file.write(f"Report: {data}")


if __name__ == '__main__':
    report_generator = ReportGenerator()
    report_saver = ReportSaver()

    report_generator.generate_report("Sales Data")
    report_saver.save_to_file("Sales Data")
