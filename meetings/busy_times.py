import arrow


def busy_times(things, startOfRange, endOfRange):
  timeslots = []

  for entry in things:

    #busy time
    if "transparency" not in entry:
      #all day event
      if "date" in entry["start"]:
        summary = entry["summary"]
        start = entry["start"]["date"] + "00:00:00" + startOfRange[19:]
        end = entry["end"]["date"] + "23:59:00" + endOfRange[19:]
      else:
        #normal event
        summary = entry["summary"]
        start = entry["start"]["dateTime"]
        end = entry["end"]["dateTime"]
      
      #event is either directly in range or on either edges
      inRange = (endOfRange > end) and (startOfRange < start)
      edgeRange = (startOfRange > start) and (startOfRange < end)
      otherEdgeRange = (endOfRange > start) and (endOfRange < end)
      
      if (inRange or edgeRange or otherEdgeRange):
        event = {"summary":summary, "start":start, "end":end }
        timeslots.append(event)

  return timeslots