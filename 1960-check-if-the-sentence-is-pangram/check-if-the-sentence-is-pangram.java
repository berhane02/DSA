import java.util.*;

class Solution {
    public boolean checkIfPangram(String sentence) {
        Set<Character> present = new HashSet<>();
        for (char c : sentence.toCharArray()) {
            present.add(c);
        }
        return present.size() == 26;
    }
}

