# Gallery Subdomain Traffic

# Your gallery has been trying to increase it's online presence by hosting several virtual galleries. 
# Each virtual gallery's web traffic is tracked through domain names, where each domain may have subdomains.

# A domain like "modern.artmuseum.com" consists of various subdomains. 
# At the top level, we have "com", at the next level, we have "artmuseum.com", 
# and at the lowest level, "modern.artmuseum.com". 
# When visitors access a domain like "modern.artmuseum.com", 
# they also implicitly visit the parent domains "artmuseum.com" and "com".

# A count-paired domain is represented as "rep d1.d2.d3" where rep is the number of visits to the domain and d1.d2.d3 is the domain itself.
#    For example, "9001 modern.artmuseum.com" indicates that "modern.artmuseum.com" was visited 9001 times.
# Given an array of count-paired domains cpdomains, return an array of the count-paired domains of each subdomain. The order of the output does not matter.

from collections import Counter

def subdomain_visits(cpdomains):
    subdomain_count = Counter()
    result = []

    for entry in cpdomains:
        parts = entry.split()
        count = int(parts[0])
        domain = parts[1]

        subdomains = domain.splits(".")

        for i in range(len(subdomains)):
            current_subdomain = ".".join(subdomains[i:])
            subdomain_count[current_subdomain] += count
    
    for subdomain, total_count in subdomain_count.items():
        result.append(f"{total_count} {subdomain}")

    return result

cpdomains1 = ["9001 modern.artmuseum.com"]
cpdomains2 = ["900 abstract.gallery.com", "50 impressionism.com", 
              "1 contemporary.gallery.com", "5 medieval.org"]

print(subdomain_visits(cpdomains1))
print(subdomain_visits(cpdomains2))