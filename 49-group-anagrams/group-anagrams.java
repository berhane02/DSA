class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        if (strs == null || strs.length == 0) return new ArrayList<>();

        Map<String, List<String>> anagrams = new HashMap<>();

        for (String word: strs){

            char[] sortWord = word.toCharArray();
            Arrays.sort(sortWord);
            String sorted = new String(sortWord);

            if(!anagrams.containsKey(sorted)){
                anagrams.put(sorted, new ArrayList<>());
            }

            anagrams.get(sorted).add(word);
        }
        return new ArrayList<>(anagrams.values());
    }
}