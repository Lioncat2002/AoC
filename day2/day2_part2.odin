package kittyaoc

import "core:fmt"
import "core:strings"
import "core:strconv"

main :: proc() {
    inputs:=string(#load("test_inputs.txt"))
    arr:=strings.split(inputs,"\n")
    pos:=[2]int{0,0}
    aim:int=0

    for i in arr{
        l:=strings.split(i," ")
        if l[0]=="forward"{
            t,e:=strconv.parse_int(l[1])
            pos[0]+=t
            pos[1]+=t*aim
        }
        if l[0]=="down"{
            t,e:=strconv.parse_int(l[1])
            aim+=t

        }
        if l[0]=="up"{
            t,e:=strconv.parse_int(l[1])
            aim-=t
        }
    }
    fmt.println(pos[0]*pos[1])
}