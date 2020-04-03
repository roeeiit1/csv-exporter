from influxdb import InfluxDBClient
import const
import csv


def convert_csv_to_list(csv_dir):
    with open(csv_dir, newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
        return data


def convert_list_to_metric(list):
    metric = {}
    metric["timestamp"] = list[0]
    metric["measurement"] = fix_csv_string(list[1])
    metric["labels"] = "".join([f"{fix_csv_string(list[i - 1])}={list[i]}," for i in range(4, len(list), 2)])[:-1]
    metric["fieldKey"] = list[2]
    return metric


def fix_csv_string(string):
    return string.replace(" ", "_")

def convert_metric_to_line(metric):
    line = f"{metric['measurement']},{metric['labels']} fieldKey={metric['fieldKey']} {metric['timestamp']}"
    return line


def get_csv_metrics(csv_dir):
    csv_list = convert_csv_to_list(csv_dir)
    metrics = [convert_list_to_metric(list) for list in csv_list]
    return [convert_metric_to_line(metric) for metric in metrics]


client = InfluxDBClient(host="localhost", port=8086, database="metrics")
for line in get_csv_metrics(const.csv_directory):
    client.write([line], {'db': "metrics"}, protocol='line')
