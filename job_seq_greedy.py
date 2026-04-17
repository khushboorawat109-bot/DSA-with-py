def job_sequencing(jobs):
    # Step 1: Sort jobs by profit (high → low)
    def get_profit(job):
        return job[2]
    jobs.sort(key=get_profit, reverse=True)

    # Step 2: Find max deadline
    max_deadline = 0
    for job in jobs:
        if job[1] > max_deadline:
            max_deadline = job[1]

    # Step 3: Create slots
    slots = [False] * max_deadline
    result = [''] * max_deadline
    total_profit = 0

    # Step 4: Place jobs
    for job in jobs:
        job_id = job[0]
        deadline = job[1]
        profit = job[2]

        for i in range(deadline - 1, -1, -1):
            if slots[i] == False:
                slots[i] = True
                result[i] = job_id
                total_profit += profit
                break
    return result, total_profit
jobs = [
    ('J1', 2, 100),
    ('J2', 1, 19),
    ('J3', 2, 27),
    ('J4', 1, 25),
    ('J5', 3, 15)
]

ans, profit = job_sequencing(jobs)

print("Jobs done:", ans)
print("Total profit:", profit)