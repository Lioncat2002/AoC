package kittyaoc

import "core:fmt"
import "core:strings"

main :: proc() {
    //inputs,err:=os.read_entire_file_from_filename("day1_inputs.txt")
    inputs:=string(#load("day1_inputs.txt"))
    arr:=strings.split(inputs,"\n")
     
    sum:int=0
    for i in 0..<len(arr)-1{
        if (arr[i+1]>=arr[i]){
            sum+=1
            fmt.println(arr[i])
            fmt.println(arr[i+1])
            
        }
    }
    fmt.printf("sum: %d", sum)
}