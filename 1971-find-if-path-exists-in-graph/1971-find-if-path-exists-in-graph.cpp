class Solution {
public:
    bool visited[200001] = {0};
    map<int, vector<int>> mp;
    bool validPath(int n, vector<vector<int>>& edges, int source, int destination) {
        for (auto a: edges){
            mp[a[0]].push_back(a[1]);
            mp[a[1]].push_back(a[0]);
        }
        dfs(source, destination, edges);
        if (visited[destination])
            return true;
        else
            return false;
    }
    void dfs(int source, int dest, vector<vector<int>>& edges)
    {
        visited[source] = true;
        if (visited[dest])
            return;
        for (int i = 0; i < mp[source].size(); i++)
        {
            if (!visited[mp[source][i]])
                dfs(mp[source][i], dest, edges);
        }
    }
    
};