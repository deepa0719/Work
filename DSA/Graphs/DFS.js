const depthFirstPrint = (graph, source) => {
    //Iterative Way
    const stack = [ source ];
        while (stack.length > 0) {
        const current = stack.pop();
        console.log(current);
        
        for (let neighbor of graph[current]) {
            stack.push(neighbor)
        }
    }
    
    //Recursive Way
    // console.log(source);
    // for (let neighbor of graph[source]) {
    //     depthFirstPrint(graph, neighbor);
    // }
};

const graph = {
    a: ['b', 'c'],
    b: ['d', 'g'],
    c: ['e', 'j'],
    d: ['f'],
    e: ['h', 'i'],
    f: [],
    g: [],
    h: [],
    i: [],
    j: []
};

depthFirstPrint(graph, 'a');
