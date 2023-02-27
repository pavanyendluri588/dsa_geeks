/*
https://leetcode.com/discuss/interview-question/2032910/juspay-oa-nearest-meeting-cell


23
4 4 1 4 13 8 8 8 0 8 14 9 15 11 -1 10 15 22 22 22 22 22 21
9 2

Sample Output :
4


*/




vector<vector<int>> edge;
int enemy, person;
set<int> st;
vector<bool> visited;
vector<bool> dirty;
void dfs (int node, int par) {
    visited[node] = true;
    for (int child: edge[node]) {
        if (!visited[child]) {
            dfs(child, node);
        }
    }
    if (par != -1) {
        dirty[par] = dirty[par] or dirty[node];
    }
        
    
}
int main() {
    int n; cin >> n;
    int sz = 0;
    for (int i = 0; i < n; ++i) {
        int node;
        cin >> node;
        sz = max(sz, node + 1);
    }
    edge.resize(sz);
    visited.resize(sz, false);
    dirty.resize(sz);
    int edges; cin >> edges;
    while (edges--) {
        int u, v;
        cin >> u >> v;
        edge[v].push_back(u);
    }
    cin >> enemy >> person;
    dirty[enemy] = true;
    dfs(person, -1);
    for (int child: edge[person]) {
        if (dirty[child]) {
            cout << child << " ";
        }
    }

}
