#include <iostream>
#include <vector>
#include <queue>
#include <tuple>

using namespace std;
typedef vector<vector<int>> vvi;

int dx[] = {0, 0, -1, 1};
int dy[] = {-1, 1, 0, 0};

void bfs(const vvi& v, vvi& visited, int i, int j, int height, int n) {
    queue<tuple<int, int>> q;
    visited[i][j] = 1;

    q.push({i, j});

    while (!q.empty()) {
        int x, y;
        tie(x, y) = q.front();
        q.pop();

        for (int k = 0; k < 4; k++) {
            int tx = x + dx[k];
            int ty = y + dy[k];


            if (tx >= 0 && tx < n && ty >= 0 && ty < n && v[tx][ty] > height && visited[tx][ty] == 0) {
                visited[tx][ty] = 1;
                q.push({tx, ty});
            }
        }
    }
}


int findSafeZone(int height, const vvi& v, int n) {
    vvi visited(n, vector<int>(n, 0));
    int count = 0;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (visited[i][j] == 0 && v[i][j] > height) {
                bfs(v, visited, i, j, height, n);
                count++;
            }
        }
    }
    return count;
}

int main() {
    int n;
    cin >> n;

    vvi v(n, vector<int>(n));


    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> v[i][j];
        }
    }

    int result = 0;


    for (int height = 0; height < 101; height++) {
        result = max(result, findSafeZone(height, v, n));
    }


    cout << result << endl;

    return 0;
}
