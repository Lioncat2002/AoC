package kittyaoc

import "core:fmt"
import "core:strings"
import "core:strconv"
main :: proc() {
    //inputs,err:=os.read_entire_file_from_filename("day1_inputs.txt")
    inputs:=string(#load("day1_inputs.txt"))
    arr:=strings.split(inputs,"\n")
     
    sum:int=0
    for i in 1..<len(arr){
        tempi,err:=strconv.parse_int(arr[i])
        tempi1,err1:=strconv.parse_int(arr[i-1])
        if (tempi>tempi1){
            sum+=1
            fmt.println(arr[i])
            fmt.println(arr[i+1])
            
        }
    }
    fmt.printf("sum: %d", sum)
}