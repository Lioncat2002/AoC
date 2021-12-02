package kittyaoc

import "core:fmt"

main :: proc() {
    inputs:=[22]int{156,176,175,176,183,157,150,153,154,170,162,167,170,188,190,194,196,198,202,203,187,189}
    sum:int=0
    for i in 0..<21{
        if (inputs[i+1]<inputs[i]){
            sum+=1
        }
    }
    fmt.printf("sum: %d", sum)
}