/*
Optimal solution in O(n) time ans O(1) memory
First count 'A' letters in the string, let this equal to num_a, hence there are n-num_a 'B' letter.
Deleting all 'A' or all 'B' is good and leaves a good string (that contains only 'B' or 'A').

Otherwise in the optimal string you see both 'A' and 'B'.
We are searching for the first 'B' in the given string.
If you see that at position=i, then before this point you should delete all 'B', and after position=i you should delete all 'A'.
But if you process the characters one by one you'll know these counts, so you'd need to delete del+num_a, where for del you need to increase it one if you see 'B', and decrease num_a by one if you see 'A'.

*/

int abletters(string s){

    int n=s.length();
    int num_a=0,ans;

    for(int i=0;i<n;i++)
        if(s[i]=='A') num_a++;
    ans=min(num_a,n-num_a);

    int del=0;
    for(int i=0;i<n;i++){
        if(s[i]=='B'){
            ans=min(ans,del+num_a);
            del++;
        }
        else num_a--;
    }
    return ans;
}


int main(void){

    cout<<abletters("BAAABAB")<<endl;
    cout<<abletters("BBABAA")<<endl;
    cout<<abletters("AABBBB")<<endl;

    return 0;
}
// output 2 3 0