import os
from datetime import datetime
from itertools import groupby

import matplotlib.pyplot as plt
from arcgis.gis import GIS

def _main():
    g = GIS(profile="python_playground")
    server = g.admin.servers.list()[0]
    messages = server.logs.query(datetime.now().isoformat(),
                                 level="SEVERE")["logMessages"]
    grouped_messages = _group_by_code(messages)
    _output_graph_image(grouped_messages)

def _group_by_code(messages):
    output = {}
    for key, group in groupby(messages, lambda x: x["code"]):
        if key in output:
            output[key].append(list(group)[0])
        else:
            output[key] = [ list(group)[0] ]
    return output

def _output_graph_image(grouped_messages):
    fig, ax = plt.subplots()
    plt.bar(list(str(x) for x in grouped_messages.keys()),
            list(len(x) for x in grouped_messages.values()))
    fig.autofmt_xdate()
    fig.savefig("output.png")
    print("{}/output.png written succesfully!".format(
        os.path.dirname(os.path.realpath(__file__))))

if __name__ == "__main__":
    _main()
