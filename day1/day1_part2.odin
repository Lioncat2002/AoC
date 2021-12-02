package kittyaoc

import "core:fmt"
import "core:strings"
import "core:strconv"

main :: proc() {
    //inputs,err:=os.read_entire_file_from_filename("day1_inputs.txt")
    inputs:=string(#load("day1_inputs.txt"))
    arr:=strings.split(inputs,"\n")
    final:[2000]int
    sum:int=0
    for i in 1..<len(arr)-1{
        i1,e1:=strconv.parse_int(arr[i-1])
        i2,e2:=strconv.parse_int(arr[i])
        i3,e3:=strconv.parse_int(arr[i+1])
        
        final[i]=i1+i2+i3
        
    }
    for i in 2..<len(final){
        fmt.println(final[i])
        if final[i-1]<final[i]{
            sum+=1
        }
    }
    fmt.printf("sum: %d", sum)
}