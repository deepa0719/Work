const hasPath = (graph, source, dest) => {
    //Iterative Way DFS
    // const stack = [ source ];
    // while (stack.length > 0) {
    //     const current = stack.pop()
    //     if (current === dest) {
    //         return true
    //     }
    //     for (let neighbor in graph[current]) {
    //         stack.push(neighbor)
    //     }
    // }
    // return false

    //Recursive Way DFS
    if (source === dest) return true;

    for(let neighbor of graph[source]) {
        if (hasPath(graph, neighbor, dest) === true) {
            return true;
        }
    }
    return false;
};

//BFS Approach
// const hasPath = (graph, src, dst) => {
//     const queue = [ src ];

//     while (queue.length > 0) {
//         const current = queue.shift();
//         if (current === dst) return true;
//         for (let neighbor of graph[current]) {
//             queue.push(neighbor);
//         }
//     }
// };

console.log(hasPath())
const graph = {
    f: ['i', 'g'],
    g: ['h'],
    h: [],
    i: ['g','k'],
    j: ['i'],
    k: []
}