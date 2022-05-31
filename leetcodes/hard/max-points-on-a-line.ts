/**
 * @source: https://leetcode.com/problems/max-points-on-a-line/
 * @param {number[][]} points
 * @return {number}
 */


function maxColinear(focus:number[], points:number[][]):number{
    const slopes = points.map((x)=>(x[0]-focus[0])/(x[1]-focus[1]))
    let slope_counts = {}
    slopes.forEach(function(i) {
        if(slope_counts[i] === undefined)
            slope_counts[i] = 0
        slope_counts[i] += 1
    })
    let temp:number[] = Object.values(slope_counts);
    let answer = Math.max(...temp) + 1;
    return answer
    
    
}

function maxPoints(points: number[][]):number{
    if (points.length > 2){
        let focus = points.pop();
        return Math.max(maxColinear(focus,points),maxPoints(points))
    }else{
        return points.length;
    }
    
};
