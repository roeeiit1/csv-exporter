from prometheus_client.core import GaugeMetricFamily
import csv


def convert_csv_to_list(csv_dir):
    with open(csv_dir, newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
        return data


def build_gauges(csv_list):
    gauges = {}
    for list in csv_list:
        metric_name = fix_csv_string(list[1])
        gauges[metric_name] = GaugeMetricFamily(metric_name, metric_name,
                                                labels=[fix_csv_string(list[i]) for i in range(3, len(list), 2)])
    return gauges


def convert_list_to_metric(list):
    metric = {}
    metric["timestamp"] = list[0]
    metric["value"] = list[2]
    metric["labels"] = [list[i] for i in range(4, len(list), 2)]
    return metric


def fix_csv_string(string):
    return string.replace(" ", "_")


def get_csv_metrics(csv_dir):
    csv_list = convert_csv_to_list(csv_dir)
    gauges = build_gauges(csv_list)
    metrics = [(fix_csv_string(list[1]), convert_list_to_metric(list)) for list in csv_list]
    for metric in metrics:
        gauges[metric[0]].add_metric(**metric[1])
    return gauges


class CsvCollector(object):
    def __init__(self, csv_dir):
        self.csv_dir = csv_dir

    def collect(self):
        gauges = get_csv_metrics(self.csv_dir)
        for gauge in gauges.values():
            yield gauge
