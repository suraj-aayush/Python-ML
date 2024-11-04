#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

class FenwickTree {
public:
    FenwickTree(int size) : size(size) {
        tree.resize(size + 2, 0);
    }

    void update(int index, int delta = 1) {
        while (index <= size) {
            tree[index] += delta;
            index += index & -index;
        }
    }

    int query(int index) {
        int res = 0;
        while (index > 0) {
            res += tree[index];
            index -= index & -index;
        }
        return res;
    }

    int range_query(int left, int right) {
        if (left > right) return 0;
        return query(right) - query(left - 1);
    }

private:
    int size;
    vector<int> tree;
};

int getInaccurateProcesses(const vector<int>& processOrder, const vector<int>& executionOrder) {
    int n = processOrder.size();
    unordered_map<int, int> pid;
    for (int idx = 0; idx < n; ++idx) {
        pid[processOrder[idx]] = idx;
    }

    FenwickTree ft(n);
    int inaccurate = 0;
    for (int process : executionOrder) {
        int index = pid[process];
        int fti = index + 1;
        int count = ft.query(fti - 1);
        if (count != index) {
            inaccurate++;
        }
        ft.update(fti);
    }

    return inaccurate;
}

int main() {
    int n;
    cout << "Enter the number of processes: ";
    cin >> n;

    vector<int> processOrder(n);
    vector<int> executionOrder(n);

    cout << "Enter process order as space-separated integers: ";
    for (int i = 0; i < n; ++i) {
        cin >> processOrder[i];
    }

    cout << "Enter execution order as space-separated integers: ";
    for (int i = 0; i < n; ++i) {
        cin >> executionOrder[i];
    }

    int result = getInaccurateProcesses(processOrder, executionOrder);
    cout << "Number of inaccurate processes: " << result << endl;

    return 0;
}
