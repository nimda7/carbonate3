from functools import partial

map_long = partial(map, lambda m: ':'.join(map(str, m)))
map_short = partial(map, lambda m: m[0])


def filter_metrics(inputs, node, cluster, invert=False, filter_long=False):
    if isinstance(node, (str, bytes)):
        match = [node]
    else:
        match = node

    for metric_name in inputs:
        dests = list(cluster.get_destinations(metric_name))
        dests = set(map_long(dests)) | set(map_short(dests))

        if dests & set(match):
            if not invert:
                yield metric_name
        else:
            if invert:
                yield metric_name
