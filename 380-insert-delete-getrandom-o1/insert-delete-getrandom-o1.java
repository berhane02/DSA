import java.util.*;

class RandomizedSet {
    private Map<Integer, Integer> numMap;
    private List<Integer> listNum;
    private Random random;
    
    public RandomizedSet() {
        numMap = new HashMap<>();
        listNum = new ArrayList<>();
        random = new Random();
    }
    
    public boolean insert(int val) {
        boolean res = !numMap.containsKey(val);
        if (res) {
            numMap.put(val, listNum.size());
            listNum.add(val);
        }
        return res;
    }
    
    public boolean remove(int val) {
        boolean res = numMap.containsKey(val);
        if (res) {
            int idx = numMap.get(val);
            int lastVal = listNum.get(listNum.size() - 1);
            listNum.set(idx, lastVal);
            numMap.put(lastVal, idx);
            listNum.remove(listNum.size() - 1);
            numMap.remove(val);
        }
        return res;
    }
    
    public int getRandom() {
        return listNum.get(random.nextInt(listNum.size()));
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * boolean param_1 = obj.insert(val);
 * boolean param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */

