class Solution {
public:
    string simplifyPath(string p) {
        int n= p.length();
        
        
        stack<string> s;
        s.push("/");
        int dircount=1;
        for(int i=1;i<n;){
            int c=p[i];
            
            if(p[i]=='.'){
                int count =0;
                string temp="";
                bool folder=false;
                while(i<n && p[i]!='/'){
                    if(p[i]!='.'){
                        folder=true;
                    }
                    temp+=p[i];
                    count++;
                    i++;
                }
                
                if(folder){
                    s.push(temp);
                    dircount++;
                }
                else if(count==2){
                    if(dircount>1){
                        s.pop();
                        dircount--;
                    }
                }
                else if(count>2){
                    s.push(temp);
                    dircount++;
                }
            }
            else if(p[i]=='/'){
                i++;
            }
            else{
                string temp= "";
                while(i<n && p[i]!='/'){
                    temp+=p[i];
                    i++;
                }
                s.push(temp);
                dircount++;
            }
            
        }
        string ans="";
        while(!s.empty()){
            if(ans==""){
                ans=s.top();
            }
            else{
                if(s.top()!="/"){
                    ans = s.top()+"/" + ans;
                }
                else{
                    ans= "/"+ans;
                }
                
            }
            s.pop();
        }
        return ans;
    }
};