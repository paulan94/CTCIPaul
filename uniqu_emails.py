
x = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]

def unique(emails):
    ans = set()
    for email in emails:
        local, domain = email.split('@')[0], email.split('@')[1]
        print (local, domain)
        local = local.replace('.', '')
        if '+' in local:
            local = local.split('+')[0]
        ans.add(local+ '@'+ domain)
    print (ans)
    return len(ans)


print (unique(x))
