import java.util.*;

class Solution {
    public String[] reorderLogFiles(String[] logs) {
        List<String[]> letterLogs = new ArrayList<>();
        List<String> digitLogs = new ArrayList<>();
        
        for (String log : logs) {
            int firstSpace = log.indexOf(' ');
            String identi = log.substring(0, firstSpace);
            String rest = log.substring(firstSpace + 1);
            
            if (Character.isLetter(rest.charAt(0))) {
                letterLogs.add(new String[]{rest, identi, log});
            } else {
                digitLogs.add(log);
            }
        }
        
        letterLogs.sort((a, b) -> {
            int cmp = a[0].compareTo(b[0]);
            if (cmp != 0) return cmp;
            return a[1].compareTo(b[1]);
        });
        
        List<String> result = new ArrayList<>();
        for (String[] entry : letterLogs) {
            result.add(entry[2]);
        }
        result.addAll(digitLogs);
        
        return result.toArray(new String[0]);
    }
}

