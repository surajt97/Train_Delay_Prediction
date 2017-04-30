quer = "imsi=gt"
query_components = dict(qc.split("=") for qc in quer.split("&"))
imsi = query_components["imsi"]
