const fs = require('fs');

const data = fs.readFileSync('../input/18.in', 'utf-8');
const lines = data.split('\n')
    .filter(s => s.includes(","))
    .map(s => s.split(',').map(x => Number(x)));

const n = 71;

function check(last_index) {
    let game = new Array(n).fill(null).map(() => new Array(n).fill(0));
    let dis = new Array(n).fill(null).map(() => new Array(n).fill(Infinity));
    let vis = new Array(n).fill(null).map(() => new Array(n).fill(false));
    
    let dirs = [[-1, 0], [1, 0], [0, 1], [0, -1]];
    
    
    lines.forEach(([x, y], i) => {
        if (i <= last_index) {
            game[x][y] = 1;
        }
    })
    
    
    dis[0][0] = 0;
    
    for (let i = 0; i < n * n; i++) {
        let minDis = Infinity;
        let u = -1, v = -1;
        for (let j = 0; j < n; j++) {
            for (let k = 0; k < n; k++) {
                if (!vis[j][k] && dis[j][k] < minDis) {
                    minDis = dis[j][k];
                    u = j; v = k;
                }
            }
        }
    
        if (u === -1 && v === -1) break;
    
        vis[u][v] = true;
    
        dirs.forEach(([dx, dy]) => {
            let nu = u + dx;
            let nv = v + dy;
    
            if (!(0 <= nu && nu < n && 0 <= nv && nv < n)) return;
            if (game[nu][nv] === 1) return;
    
            const newDis = dis[u][v] + 1;
            if (newDis < dis[nu][nv]) {
                dis[nu][nv] = newDis;
                if (nu == n - 1 && nv == n - 1 && newDis < Infinity) {
                    return true;
                }
            }
        })
    }
    
    return dis[n - 1][n - 1] !== Infinity;
}


// Do binary search as if it's 2018

let l = 1023;
let r = lines.length - 1;

while (l < r) {
    let mid = (l + r) >> 1;
    if (check(mid)) l = mid + 1;
    else r = mid;
}

console.log(lines[l].join(","));
