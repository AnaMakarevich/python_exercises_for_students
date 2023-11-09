class Report:
    def generate_report(self, data):
        print(f"Generating report for {data}")

    def save_to_file(self, data):
        with open("report.txt", "w") as file:
            file.write(f"Report: {data}")


if __name__ == '__main__':
    report_generator = Report()
    report_generator.generate_report("Sales Data")
    report_generator.save_to_file("Sales Data")
