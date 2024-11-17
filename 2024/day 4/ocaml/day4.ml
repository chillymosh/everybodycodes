let read_file filename =
  let ic = open_in filename in
  let rec loop acc =
    try
      let line = input_line ic in
      let number = int_of_string line in
      loop (number :: acc) 
    with
    | End_of_file -> List.rev acc
    | e ->  
      close_in_noerr ic; 
      raise e
  in
  try
    let numbers = loop [] in
    close_in ic; 
    numbers
  with exc -> 
    raise exc


(* This is how you would manually find min number instead of `List.fold_left min max_int data` *)
let find_min_num list_nums =
  let rec find_min_aux current_min = function
    | [] -> current_min
    | x :: xs -> find_min_aux (if x < current_min then x else current_min) xs
  in
  match list_nums with
  | [] -> None
  | first :: rest -> Some (find_min_aux first rest)


let median list_nums =
  match List.sort compare list_nums with
  | [] -> None
  | sorted ->
    let len = List.length sorted in
    if len mod 2 = 1 then
      Some (List.nth sorted (len / 2))
    else
      let mid1, mid2 = List.nth sorted ((len / 2) - 1), List.nth sorted (len / 2) in
      Some ((mid1 + mid2) / 2)



let min_hits filename part_num =
  let data = read_file filename in
  match part_num with
  | 1 | 2 ->
    let min_num = List.fold_left min max_int data in
    List.fold_left (fun acc x -> acc + x - min_num) 0 data
  | _ ->
    match median data with
    | Some med ->
      List.fold_left (fun acc x -> acc + (abs (x - med))) 0 data
    | None ->
      0 


let () =
  let p1 = min_hits "../everybody_codes_e2024_q04_p1.txt" 1 in
  Printf.printf "Part 1: %d\n" p1;

  let p2 = min_hits "../everybody_codes_e2024_q04_p2.txt" 2 in
  Printf.printf "Part 2: %d\n" p2;

  let p3 = min_hits "../everybody_codes_e2024_q04_p3.txt" 3 in
  Printf.printf "Part 3: %d\n" p3;