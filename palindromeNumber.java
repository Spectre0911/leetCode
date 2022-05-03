class Solution {
    public boolean isPalindrome(int x) {
        
        
        if (x < 0) {
            return false;
        }
        
        String y = Integer.toString(x);

        int tail = y.length() ;
        int half = Math.floorDiv(tail, 2);
        
        for (int head = 0; head < half; head++){
                     
          

            if (y.charAt(head) != y.charAt(tail-1)){
                return false;
             }
            
            tail--;
        }
        
        
    
        return true;
        
    }
}