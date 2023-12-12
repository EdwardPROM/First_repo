from collections import Counter

def get_count_visits_from_ip(ip_list):
    return dict(Counter(ip_list))

def get_frequent_visit_from_ip(ip_list):
    ip_counts = Counter(ip_list)
    most_common_ip, count = ip_counts.most_common(1)[0]
    return most_common_ip, count

# Приклад використання:
IP = [
    "85.157.172.253",
    "66.50.38.43",
    "85.157.172.253",
    "66.50.38.43",
    "66.50.38.43",
    "66.50.38.43",
    "192.168.1.1",
]

count_visits = get_count_visits_from_ip(IP)
print(count_visits)

frequent_visit = get_frequent_visit_from_ip(IP)
print(frequent_visit)
