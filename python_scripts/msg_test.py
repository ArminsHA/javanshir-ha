# `data` is available as builtin and is a dictionary with the input data.
name = data.get("name", "Hoppsan")
# `logger` and `time` are available as builtin without the need of explicit import.
logger.info("Data {} at {}".format(name, time.time()))
