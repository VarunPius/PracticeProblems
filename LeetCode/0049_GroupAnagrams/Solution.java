public class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        if(strs == null||strs.length == 0)
            return new ArrayList<List<String>>();

        Map<String, List<String>> map = new HashMap<String, List<String>>();

        for(String s: strs ){
            char[] ch = s.toCharArray();
            Arrays.sort(ch);
            String tmp = String.valueOf(ch);
            if(!map.containsKey(tmp))
                map.put(tmp, new ArrayList<String>());
            map.get(tmp).add(s);
        }
        return new ArrayList<List<String>>(map.values());
    }
}
