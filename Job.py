class Job:
    def __init__(self, source, date_posted, job_title, company, link):
        self.source = source
        self.date_posted = date_posted
        self.job_title = job_title
        self.company = company
        self.link = link


J = Job(1,"11/07/2018:18:03", "Software Engineer", "Google", "www.google.com")

