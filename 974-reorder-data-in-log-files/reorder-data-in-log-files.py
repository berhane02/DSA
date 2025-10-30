class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        letter_logs, digit_logs = [], []

        for log in logs:
            ideti, rest = log.split(' ',1)

            if rest[0].isalpha():
                letter_logs.append((rest,ideti, log))
            else:
                digit_logs.append(log)

        letter_logs.sort(key=lambda x:(x[0],x[1]))

        return [log for ideti, rest, log in letter_logs]+digit_logs
