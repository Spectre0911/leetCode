class Solution {
    public String longestCommonPrefix(String[] strs) {
        
        if (strs.length == 0) {
            return "";
        }
        
        // get min size out of all strings
        // O(n)
        int minSize = strs[0].length();
        
        for (int i=1; i<strs.length;i++){
            if (strs[i].length() < minSize){
                minSize = strs[i].length();
            }
            
        }
        
        String prefix = "";
        
        for (int j=0;j<minSize;j++){
            
            char initial = strs[0].charAt(j);

            for (String str: strs){
                
                if (str.charAt(j) != initial){
                    return prefix;
                
                }
                
            }
            
            prefix += initial;
         
            
        }
        
        return(prefix);
        
      
    }
}