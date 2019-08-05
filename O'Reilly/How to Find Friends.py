def check_connection(network, first, second):
    team = {first}

    #for _ in network:
    for edge in network:
        pair = set(edge.split('-'))
        if pair & team:
            team |= pair

    return second in team

print(check_connection(
	("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
	 "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
	"scout2", "scout3"))
print(check_connection(
	("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
	 "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
	"dr101", "sscout"))
    