let read_file_first_line filename =
  let channel = open_in filename in
  try
    let line = input_line channel in
    close_in channel;
    line  
  with e ->
    close_in_noerr channel; 
    raise e 

(* Part 1 *)

let file_path = "../everybody_codes_e2024_q01_p1.txt";;
let notes = read_file_first_line file_path;;

let char_values = Array.make 256 0;;
char_values.(Char.code 'A') <- 0;;
char_values.(Char.code 'B') <- 1;;
char_values.(Char.code 'C') <- 3;;
char_values.(Char.code 'D') <- 5;;
char_values.(Char.code 'x') <- 0;;

let p1 = String.fold_left (fun acc x -> acc + char_values.(Char.code x)) 0 notes;;
Printf.printf "Part 1: %d\n" p1;;


(* Part 2 *)

let file_path = "../everybody_codes_e2024_q01_p2.txt";;
let notes = read_file_first_line file_path;;

(* let sum_pairs notes char_values =
  let len = String.length notes in
  let rec loop idx acc =
    if idx >= len - 1 then acc
    else
      let char1 = notes.[idx] in
      let char2 = notes.[idx + 1] in
      let value1 = char_values.(Char.code char1) in
      let value2 = char_values.(Char.code char2) in
      let extra = if char1 != 'x' && char2 != 'x' then 2 else 0 in
      loop (idx + 2) (acc + value1 + value2 + extra)
  in
  loop 0 0 *)


let sum_multi notes char_values part_no =
  let len = String.length notes in
  let rec loop idx acc =
    if idx >= len then acc
    else
      let char1 = notes.[idx] in
      let char2 = notes.[idx + 1] in
      let step_size, extra = match part_no with
        | 2 ->
          let extra = if char1 <> 'x' && char2 <> 'x' then 2 else 0 in
          (2, extra)
        | 3 when idx + 2 < len ->
          let char3 = notes.[idx + 2] in
          let extra = match (char1, char2, char3) with
            | ('x', 'x', _) | ('x', _, 'x') | (_, 'x', 'x') -> 0
            | ('x', _, _) | (_, 'x', _) | (_, _, 'x') -> 2
            | _ -> 6 in
          (3, extra)
        | 3 -> (3, 0)
        | _ -> failwith "Invalid part number"
      in
      let total_value = char_values.(Char.code char1) + char_values.(Char.code char2) +
                        (if step_size = 3 && idx + 2 < len then char_values.(Char.code (notes.[idx + 2])) else 0) in
      loop (idx + step_size) (acc + total_value + extra)
  in
  loop 0 0




let p2 = sum_multi notes char_values 2;;
Printf.printf "Part 2: %d\n" p2;;

(* Part 3 *)

let file_path = "../everybody_codes_e2024_q01_p3.txt";;
let notes = read_file_first_line file_path;;

(* let sum_triples notes char_values =
  let len = String.length notes in
  let rec loop idx acc =
    if idx >= len - 2 then acc
    else
      let char1 = notes.[idx] in
      let char2 = notes.[idx + 1] in
      let char3 = notes.[idx + 2] in
      let value1 = char_values.(Char.code char1) in
      let value2 = char_values.(Char.code char2) in
      let value3 = char_values.(Char.code char3) in
      let extra = match (char1, char2, char3) with
        | ('x', 'x', _) | ('x', _, 'x') | (_, 'x', 'x') -> 0 
        |  ('x', _, _) | (_, 'x', _) | (_, _, 'x') -> 2 
        | _ -> 6 in
      loop (idx + 3) (acc + value1 + value2 + value3 + extra)
  in
  loop 0 0 *)


let p3 = sum_multi notes char_values 3;;
Printf.printf "Part 2: %d\n" p3;;