
let calc_min_dots num dots =
  let inf = max_int in
  let min_dots = Array.make (num + 1) inf in
  min_dots.(0) <- 0;
  for amount = 1 to num do
    Array.iter (fun dot ->
        if dot <= amount then
          min_dots.(amount) <- min min_dots.(amount) (min_dots.(amount - dot) + 1)
      ) dots
  done;
  min_dots.(num)

  let compute_min_dots brightness dots =
    let inf = max_int in
    let min_dots = Array.make (brightness + 1) inf in
    min_dots.(0) <- 0;
    for amount = 1 to brightness do
      Array.iter (fun dot ->
        if dot <= amount then
          let candidate = min_dots.(amount - dot) + 1 in
          if candidate < min_dots.(amount) then
            min_dots.(amount) <- candidate
      ) dots
    done;
    Printf.printf "Min dots: %s\n" (String.concat "; " (Array.to_list (Array.map string_of_int min_dots)));
    min_dots
  
  let find_optimal_split brightness dots =
    let min_dots = compute_min_dots brightness dots in
    let inf = float_of_int max_int in
    let min_total_beetles = ref inf in
    let best_split = ref None in
  
    for i = 0 to brightness / 2 do
      let j = brightness - i in
      if abs (i - j) <= 100 then
        let total_beetles = float_of_int (min_dots.(i) + min_dots.(j)) in
        Printf.printf "Checking split: (%d, %d) with total beetles %f\n" i j total_beetles;
        if total_beetles < !min_total_beetles then
          min_total_beetles := total_beetles;
          best_split := Some (i, j)
    done;
  
    match !best_split with
    | Some (i, j) -> (float_of_int min_dots.(i), float_of_int min_dots.(j), Some (i, j))
    | None -> (inf, inf, None)
  
  let process_file file_path dots =
    let notes = read_file file_path in
    List.fold_left (fun acc brightness ->
      Printf.printf "Processing brightness: %d\n" brightness;
      let beetles1, beetles2, _ = find_optimal_split brightness dots in
      acc +. beetles1 +. beetles2
    ) 0.0 notes
  
let () =
  let dots = [|1; 3; 5; 10|] in
  let notes = read_file "../part1.txt" in
  let p1 = List.fold_left (fun acc b -> acc + calc_min_dots b dots) 0 notes in
  Printf.printf "Result for part 1: %d\n" p1;

  let dots = [|1; 3; 5; 10; 15; 16; 20; 24; 25; 30|] in
  let notes = read_file "../part2.txt" in
  let p2 = List.fold_left (fun acc b -> acc + calc_min_dots b dots) 0 notes in
  Printf.printf "Result for part 2: %d\n" p2;
  
  let dots = [|1; 3; 5; 10; 15; 16; 20; 24; 25; 30; 37; 38; 49; 50; 74; 75; 100; 101|] in
  let total_beetles = process_file "../part3.txt" dots in
  Printf.printf "Total beetles required: %f\n" total_beetles