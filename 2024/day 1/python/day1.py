from itertools import batched

# Part 1
d = {"A": 0, "B": 1, "C": 3}

notes = "CCAABBACCCCCCBCACCABABBAACBCABCCBBCBBBAACBBAACBBBACACACABAACCCBCACCCCABAABCCAAACCCAAACAACCCCAABCCAABABCCAAACCABCCBCBABBBACACBAACCACAAACBCCACCBCBAAACCACCAACCAABCCCAAAACABCAABBAACCBCBBCBCBACCACAABCBABBBBACAABAAACBCBAAABBCCABBACBCBCAAACAAABABCBBBACBBCCBBABABACABBCCABAACABBCACCBCBCCCABAAACBACCBBAAACCCACCABBCBAACAAAABBCACCBBACBABCCACBCCACBACAAACCCBCCBACABABAABCACABBACBCCABBABBCBBCAABABCCBBAACBBBBBBCCCCBCACACBCCCBACABABCCCCCACBCAABBCACCBCBACBCBAAAAACAABCCACACBBBBAABCCBBCBCBABACBCCBBBCABCCBCACABABBCABCCBBABCACACBCACACCBAACBCCCCCABAABCABABCBBCBCCCAABCCCAACBCABAAACACCBCBBBACBAAAACBBCABCAACCACBACACCCBABABBAACCCCCACABBABACCAABAACCCBAABABACCBBCAABBBACCBACACCCBAABCAABBCBAABBBCCBABBBCCAACBACCBCCBBBABBAABCACCABCCBCCBCBACCAACCBCAABABCBCABCBCACCBCBACCACAABCAABCBABCCABBBAACBBCACBACBCCBBABACCACACACCCBCBBCBBCACBBBCCBCBBACBABCBCBACABAACABACABCBBCBACCCBCCCBAACCBABBABCBACBCBABBABBBBBCCBCBACABABCABCAACBCCBABABBACCCABCCBABABACBBCBCABCCABBBCBCBBCACABAAAACBCCBBAABABBAAABBAACBCCBABAABCACACCBBCCCACCABCCBCBABABBCAC"

p1 = sum(d[bug] for bug in notes)
print(p1)


# Part 2
d = {"A": 0, "B": 1, "C": 3, "D": 5, "x": 0}
notes = "BAAAAABABAxADBxBCDDCDBBxBBBBxBDDAxBDADCBCBCBxDDCBDBCDBABBAACBDDDCDBxABDBAAxACCACxDBDACDxBBADDDBAAACCxBCABDACCDCAADCABACDCDBCxABADDxCxxBBCAAxDCACxBDABCBCxADBCCCDxCDCCBBCxAxDDDxxDxBDCxCCADABABBAACAADBCDBDCDCCACCDDxxACAxABDBCCAAxCBADBBCCxABDBDBDBCCBAxAACxDABDBxCxCDADCACBABDBDxBBADADxAAAAADxDAxxxDCDADDDDCCxBCDCxBBxDABBBCBCBAAABBDxAABBACDDDBDABDDBCDxAABBDDABDCCACDCxDCBCACxCBDCBAxBDCBDAAACxAxDDBBCACBCBBDAACCBCCDADDBBACABADxBBDCCDCBADxBCBCBBxCDCCxDAADCACxBADAxDBxBxCxBBABCBCDCBCBAxCABBBDCBCCAxACxCABABACCBADBCDBADDADCDBDBxxDDBBAAxDxBDBBDxCADCBAxACCBDAxCxDCDBCACADCxADAABCDCDCCDxCBxBDABCCBBCACABDDDBCBBAACxDDAAABDDCxDCDDABABBCxDCCCCAAxDBCDBABDCADADBCxxDxxBAACAxDBBCxABDBCADCABDDDCBCADCADDCCACBBBAABxCCDxAADDBBDCCACBBBCCBxCDBAABCCDBDBDDDBCBADBBCBDDBBCADCBBADACBDCxCCABBDBxABDxAAAxCBxDBACDADBDCADDDDADCCDDCABDAACBBAAxCBCxCDBBBBCABBBBBCCDBCDCCBACBABDDCBDCCBCBBAADCCxDACxAADBCCDDBCDCCBAxDBBAADBxBAABBxxBABDCCAADDAxADACACADBACCCDBDBDBBxCDxxADDAABDBDDADBCDADAxBAACCDxCACAxCCBCBCCBCBBDABAACACCDAxxCDCACCDxDBDxCABAxCABDxDxCxCACAADABCDDADCBxABBCDxBCDCDACDxDCBCxBDBBDDCADADABDxBDABADCACACDBxCBCxDCAxBBAADADBBAACADDBCDCAADDADDDAACBAxCABADCCCBxABADDBCADDCCABCDDCBBDDCBACBAADCDxDDADADDCBCxxBAACADAxABxCABBBCCBDDBDDCACAADBAABCxBDADDxBDDCAAABDDADDCCDBCDxDCCCCDABBDDxADxxCCDBBAAADBDBCACDDxBACAABxxADDDCCBBDDACCADBBDAxCDBxDABACACCDDDACBAABxCBBBDAABCDxBBCDDAxABADxADBBBAACCDCDxADDxCDxBAAABCBBBxBBABxCCCxCBCBBDDAADxxCCBDBDCxCAADACCDAABCCACDBBDACBADCAABDBDBBBCADABBCBABxBBAxABBAAxCAABDDDCBBDDACDCBCABDACCAAAxCACDBACCCCABACBxCxCCBACxABBCACCAACCBDDAADBxAxxABADCBDBCDACBDBAxDABxCCxxABDADAAADDDBCBCxAADADBCBBAADxADCBDxCxxADxADADCDDACDBAxCDBxxDABCDABADDAADBABBCAACABDxACDDxCxDAABACBAACxCABDABCBDxCCBAxDBACADDBABDBDADAAxCDBCABBDCBxBAADBBAAACCxDBCDxCADABxBDxBBBCBACCAABBDBBxDAxCBCDxDACCCDCBDBADCBDBCDAAAxCDAADxCBCADAADCBCBxCABxCCDDxxCBDADADBBDCDBBCABADDDBDxAxBACAABDDBABDBACxCBBBxDACDCxCCAAAABxDBCCxDBxACBCCDCBDCACCDABAABCxABxAxDCADAAABCCDADBBABDxCDBCAAABACBDCDACxAxADxBBxBDxDxAACCCBAxDADBADCDBDDCACCDAxDCCDDDBDDBBAxACBCCCxDxCxABDB"

p2 = sum(
    d[p0] + d[p1] + (2 if p0 != "x" and p1 != "x" else 0)
    for p0, p1 in zip(notes[::2], notes[1::2])
)
print(p2)


# Part 3
notes = "DCxCBxCCACCBBBBxxBxAxAxCBxxBxCABBCBDADACCCxADCAAABBxDCxxxACBDDxxBDxxDCADBxCBBAADCBACDxCAxCxDBBBCxxCBBBAAxBCxDBBxDDABDDxBxDBBBADCBBBDCDDxBDxCDBBCBCCCDDxBCCADxxCADBBBDBCDxCAxBDBxCAxDADAxCxxCABBBACxxBxCxCAxxxxBAACDCACBxDDDDCACxACBACADBBDCCxCxABCDDAxxDADBxBCCACBxDCBACDDBDCxxBDCAxCCAABDCCDDxAAxADBxxACBCxACDCACADBAAABDBBAABACxDABADxBBBABxDCxBDBDDxCABBDxBAxDBBCxDDxACxxDBCxBBxxBxxDxCDCDACBBCBADDBDxCCBxDxxAACCBDDCxDCACBxDDCCxAxxCxxxDxBDCBDDBBxAxACDCADBCCxDCDBCBCCBxCxxxxACACxDBCCBDBCCCCBBBCDDBDBBAxADxxDABxABBBAABxDAxDCABDBxxxCxxDxAABxAAxAAxxxBABCCDCCBDBCCCACCADDCAABBDBBCDAACACxxBCACBBxBCBxBBxxBCABDxBCxDABxACAxDAxxAAxBDBxCBCCACBxABDABDAxBAAxADDBCCxDCxBACBBACBAxDxCBDxCCBCCCxDCAADCxxCDDCxxxDBBABDAxDDBDCxBACCxCCBDADCxBDDxxxBxCDBxCCBxABABDDABDCDCCBDCxxDDDCCBDCxBBCCDCCABDBAxDAABCDADDAACCxxADCxxBDBDBDAADxBBCCCDxCABACDDBxAACxxCCDADxCCDBBCBxCxxDABCDxCDABxxBACBBDBDABDxDDBADxACxACxABDAxADBBABBxAxDABAABDCxBBBDCDBABCxxABxABCDCxBDABADxxxBxDxDCCAxBCAAxxxDxADABxCDAAACADxBDxAAxACxCBADAxxBABADCxxACCxBCACBCCBCBBACBxACABDAADACBDxAxDAxDBxxCxxxBCxBCDDDxDCBBABCxCxBxACCCCBCDADBBAxDBACDCxBxBxCxBDxAxDCxDAAABACCBBCBBxBBBCCCDBxBBDDCCDDCBCCxBCCACDBAxADAxCxDCDDBAAxACCACCDxxCCBCCxBAABBBAAxxCCDCBCxBDxAxCxDxxDAxDBDAxCDBxDBCCCCABAxDDACxxACDDAAACxxBBACACAxDADDDBCxDAADxAxACxACCBBAxDAACACDDADCBDCCDADDxBAxDxCCBDxBDDDCxDABBxBCDxAAABDBADDxxCBDBCDBABBCxADCCDxxBABCCxCCBCDCxADCAAADxBDAxCCxCBBDDAADDBCBCDCBCDxDADAADBDCBBCCCCABBADDBCxDBDCAxDDDxxxxADDCDAxBxxBxCBAADCACAxxBCCxDACCxBADCxBDCxxCxAAxxAxBCBCDDxxBABCxABADDABBABBAAADBBCDADxBBxxBACDDABAxBABACCCDCCBABCDADCxADBBxCABxxxxBBDCxxAAxCCADxCABBDDACADCxBCAxDACBxDCBDCCDAADDCACAABCDADCDADDDDxCDCxCxAAxDCCDxDDBCxBADDxBDxxCxBDBxAxDDAxBDDDCAxACDCAxBBBDxBACDDDDDBBCDCACDADDCDABCDxACDAADAAAxBDDADABAAxADDxCAAxDADBxCADxDxABxBADxADDxBBBADxDCBDxDABADDDCCDCACxDCAxABDAxCDCCDCBxCBDxCBDAAxBBACBBDDCADABACxDBDCAxBCxABCDxDDxDAxDBDBADBBDCBCBCCBDDBCCDDxDCBxDDxBACxBBBxxxADxACCBBDBCDBDACAxxACCCxDxADxDBBDBDCxCCxABBCDCADADxACBAxABCDxBBxxDxCCBDxDCxDxxACxxBADBACADBDCCABxDDCxxBDxDAxDxCDBAAAxACxxxAACxxDCDBCxxCDBABBDAABACCxCDBABxBCBACAAxxACBBACAAxAACCADAAADBCxBDxAAADAxBCxDxBDABACBADxBxBDAABCCDBADxBDCCAxBxCCBCBBAxBxCBDxAADxBCxxADBBCDxCCCCAxDxABxCBDDCxADxCCDBACBDBCACCAACADDxDABxBBDADAxDBADxAxBCAABAAACxCDAxCACBCDxADABCCDxACDDDCxxCCxBxAxAADAxDDAxBBDxDBxBAABABDCDBABCxCABACBCDCBCABxABCABCAAABBCCACBAABDCCxAACDxDCCDDDBCDBBCCAAABCACDCCACDDCBBDCDBAABBxxADCDBBBBDACCDBDxADDAxCxDAADxCABCCxDxBDACDxABCACAAxDxBBACCDDDBAxBBCxBBABBDAACAAxCDCDABBBBBDxCDBABCDxxxABCxxACxCCBBBCxxACCCAACxxADxCADACDBCCDxxxCCCDAADCAxACDABAxCACDACCxDxDCADDxAAxxCBABCDCCACBAxCxxADDxADCADxCxBCDCxDADDxxxDDDCDxDAxxCxBADCxDxAxBDDBxDxBAADBBBBxDBBAABBACBACCDDBCDDAAABCBxDxBCxDxBAAAAACCCCDxBxCDADxBCACBxDBCDDxCDBAxBAxxDCABCDBCABAxCBBDDxCCxDDCDBCBxCAAABxCxBxBADBAxCDxBxABDDBDAABxxxCCxxACxxxCAxxxBCAAxxxDDDxACBDBxBBDDBACBxBACxxDBDACBBxDDCDBBDDCCDDxBADBCxCDDxDxxBACCxAxxCBADCCDxCACBACBCDADxBCDAACAxDAABxAxDAxBDBAAxxDCxCAAxDAABAxDxBCBBACxxDCxxCxBBACxxAxxACAxAAAxACxxAxxBBBADADCACBAACDBDCDCBDDBADDxxCDxCDxAxBBABxCxDDBCBxxxDDxACADAxxAABxDBCABACBBxACBDADxBAxBxCACBBDBxACABDAAxBBACABDxAxCBAxAAAACBxBDBCCDBxxCDxxCABADBAxCBxABxCBDAxCxBCAADDCCxDABBABDxCDCxABCCxxxAACCAAxxxADCDCxAABACAAAxCxCBACBAADxADDBBCDABAxxBDCBDDxACAAAAAxAADxAADBDxDCAABDDDBCDCxCAAAABDADCCDBCDBBCADxAACAADxxxDxDADCBBBDxDCCxDCCDBxxCADBCAADxBDBBxxADCDBxAABCxAxDCACADBxBABDCDCACBABCCCDDDCDACAxAxBBCxCDDxCDCCCDBBDACBxBACCADACCCxxBxCDABBxDCCDxBDBCDDBCDDxxxBDADxCDCDBDBBDCAADDDCBBDBCACxxBABxACBxABDDxBxADxxBxCxABBBCBxxCDDCxxACDAxDxxxBBAxDAACADBxDBxBCCxAABBxxBCBABABxACACxxBCBCBxxxCCBCCCAAAxBBACxADBDABDxBxBxBxxBCCxADAxxCDCBBxBxCCBAABxBDABBxxxBDxCDBCDxxDDxDxDCACBBDDAAADBCABDCDBDBDDADCDBDxBBCDDCABCCBBxAxCCABxxDCBDDABxxDCCACADCBxBACDCAAxDCBxxxDDCAAABBCBAxDACAxxDDBxxDxBACCDADCAxBAACDACxCAABxAxAACACBBxBCxxxDCDCBAAxDDxBxCDAxCDCAxxBDACABDDCABxCBxACAACxDCABABxCxBxABDDCBACxxABxBxCCxBBxCDCADDBACBDCDCBAxxBAAAxBCDCAACBxCCBxBBDBxAACDBBxBDCBBDADCxBxCxDxxBCxADAxDBxAADAxBADDADBACDBBCAxDxxDxBDBCBBADDCxACCAADxDxCABxBDCDACBCxCxABBDCBBxCAxCBCCCAADCxBCxCAxAxDBBDCCxABBDCDABADDBAAxCBACDACDxBDCABBCDBxDBCAABABCAACAACxxACCCDBADBxDCxxxxBCxxAADCCDABBACBAAACBAxBxCBCACCxACxACCCxxDCxxDDxCDADACCABxxxBxxBBDBCBDxBxAADxBxDCBDABABCCBAACxBCCCxxDxCCCADCAxBCBBxDBCxAAACDDBCDxCACCBCCCCABDDxDCABxDxBCCBxxxCxAxCADAAADBBxADCBDxxDDxACDADBDCCBCABCBxxxxxBxBBCDDCCADDCBBBCBCxAAADxxBBxBCxAABxxACAADCCACxDAABBACACCBDBDDAxABxDDBBBCxABCDACCAACCCBCBxCCxCBxxDDCCDCCBCAxCDBDDCBDCxBxDAxCCADBxxAxAABDBAxADDBxBBDBDCBADxDDADxBxDDCABAxADBBCAxDxxCDCACDDCBBCxCxAADCAAADBDCDBADACCCAAxDBxCBACCxDBDDDBAxDxxCBDxxBACDCBBDBCBAACDCxCDBCDDAxADABBBACDBxxBxCDBxxxADBxDCDBBADxxCAxACxCDCABxDAxBxDAAxDAxDxxADxBBDDCCCDCCxABBCxBxCACBDxxxACAAxxDADBDxACBCCCCBBADxxDxDxABDxxxDAADBCBCBxDxxAxCDBxCDDBCADxxAADDDBABBCAABBBxDCDDxAxCADBCBCBABxDxCDxBABxCDxCDDBBxBxBABCACxCDDxDBDBAxxxBxBxACBCAxAAxxxAAxCACBxCCxBADCxDABADACAxDxACxACBBBBACDDCAxDDDxADxxDxDCCDxCDBxBBDCDDDBxxAAxxDBCBBBCxCxCAxxADDAAxDCxAADBBACADxDDCCDBABBCBBxDDABBxCBCxCAABBDxDDCxBDBBBCDBACxDABADCDxDAxDBBxxCBCDxCDBCBDCxBABAABCDCAABBBCBBBDxxDABxCCBADAxxACCDCABCBBADBCCDBCBDBDBCxBCBADBDDBBCADDCDCCDBCDCBABDxBxAADAABACBCDABCBABxBABACDDADAxxxCDxxCBDACCCBxxxxBxCCABACxBxBBxDADBDDDBBCBADxBCBDCAxCAxAxADCADCxDAABCAxxDBADCCAxxAAxCBDxABCxCCBDBABCxCCDCACABBBxDCCBxDABDBDABABDxAxxBxDABDxBDCADCxBABDCDADDABCCDDBDxDDABACxADCABAAxBxDxCCCDxAADCBxACBxBDCABDxAxBACDDAxAxDDBxxDACDCBCxxDDDBDBBDxDBCCDDCAxxDxDxxAxBBADxBAxAAxCADDxCAACxCACxBACCCBABACADCBxxAABDCBCBDCCBxCCBCDCDBAxBBCxDxxBCABABBAxBxxxDBBBxBDBADABBxxCABDABACAxDBBACxCDDDBDADBABxADBBxDCDDBACDCxBDDACCDAxxDCDCBxDADADDDCDBACxACxCBACCCABDBxCDxDABxBxxDBCCxAAAABxxBDAxAABCDxDDBCBxBCBDxDBACxBDDxACDAAxCxBCCxCBABxCCxCDDBxBxDDxAxxABxBxAAAxACBCAADCCDBACCABxxACxCDABAxxCxABxCABADBCCDADDxBBCxBBAABCxDCADAxBDBCxCCxxBBxDxCDBADxCBDADxCDBDABxDAADxBCDxCBBCxBCxBAACxACAxCCCAAxxBBxACDCBCxxxCxxCACACCDCxBCCBAADxxCxCADBxACxxBABCDBBBADDBADCxBxDCBCCACBxDDCAxBDABBAxCDxxDDxDxBADCxCBABADAxBxxBxAAAxxCxADDBACCxxxBDABCxxBDBCxxDDBCCDxxDxABABBACDCxBDADDBDBCABCDBBCDBBBBCAxDxADxxAxxAABCxxxACBCDBADBBAAxBADCCBBBBDDDBBBxxxAADBDCBBBBCACAxBDCDCCxBADDCDACxACxBDBCDCAADCABAAAABxADAABBACBxAxDBCCCDDxCABDDBBCDDDBxBCxCABCBBxCBCBxCAABABDxxCDCxxCDBAADABADACxxCDCxCCBBCBBADxCBCAxABDBACBDCADADxABAxDCCxxDDCADCCCCCDxDDADAAxCAACADCxADDDDCAACDBDBAxBxBBBxDxCCADBBBBDADDCCDxBBDAAxBBxxxABDCDDABDABxBABBBCDCBBADBCxCCBBBBDBxABDCDxBDAABBDDxCCADDxDxxxxDAAACACxxAACxCCCDBAADDCBAxxxCAxDABBCxAxAADABDAxBCBDDBxxxxDDCBxAABxABxADBBxxxxxxDBBACABxxBxxxADCBxACDDBCADABxBAACADDxABxxCADDCDBBBDACCCAxCxACBADCCxDBACxBDBDBAADDAADDDBDAxCDCBCAxBDCCADBDBACxDBBxABDxDBBDCxDBxCDBCCCABCxCBBDxACDACxDAxABADDxDACBBBAAxDBAAAxBBDBDABACCDDxDBADxBxDBCDAABCCBAxAxxBxxCDAxBADACDBxADACDDDBxCCBxxDxBDCCxDDBCBxDxDDDDxDAADxCxCABACCBxCDCCBxBBBxxCDxBDBABCBBDxxCACCxACDADDDBxxCCxCCDxDAxxDxACDABDxACBCCxDCDBxxBBBBAAABAABAxBxxCBCADBCDCxCBCDBBBxxDDDDAxxxBxBxABCxxABACBDADxBCAAAxDABCxxBDDDxACCDBCDDxBxDxCxxDBxxABCxBBDCBCACAAxADxCAxACACBxCCDCxCCACCxDxxADBDBCABxxBxCBCxDxADBDADACDDADxDDCBCDDDACBxABxxxCCCxCxBBCBACBxxCBBDBxDxBxBADDxADDABCDBxBxAAxCCCxCDACBDACAABCCxDDCCDABxCCCCBDDBCABxCDAxBAABxCCCCADxCDCACDCBxxCABDADDACCDxxBDDxABBBACBCABBxCxBCxxxCBxBDAxBACDBADADCBxBxBAABAxCAAADxxABDAxxDCxABCBAxDxDCAxxBxxBBAADDCCBAxDBxCDBAxxCCBxCBCDxBxDDCDAAACACACABxDBCCBxCDACCABAxCxxBCDCADCxDxDADCDxDDBCADDAxCCDAxxAxxCABBBxBCABBCACCADCABDACBxxAADACACCxBABxDBCAxBxBAABxCxDCCDxDCBxxBDCBxCBCADxxCAxACAAAAxDxCxxxADDxxCCDCDDxAxxDDDxBBxxBxACBDxDCBBACAABBCACBCCxACxxDCCAACABCBABBCDCxDDAAABDDBxBxBADDDADBBACBBCAxAxCABACCAxDADBCxxABxADBBxAADBBxxBADACDBADxACDxCACADBBBBxBCDCDABxCDCADBxBADDDBxACCADADxCBBxBDxBCDACAxABCCBDxADCxCxDADDBBAADxxCDxBBBCDCxABCDBDCABAACBCxAABxBBDxDABDBCCCADCAxCBxDxBACCBxACxDAACADxxBADxABABBDCxCAxAADCBCBCDDBDCCxADDACBCAxxBDAxCCxACDDABDDxCBCCAAAADAACCAxADAxDDACBCDDCDBxxBxAxDxDBDCCBCCADBCCBxCBCCCBxAAxxDBBDxBxAxDxBCDDDxxDBADBCBACDDDCxAxADCCBxCBBDBDADBBxxDDBDDBCBCCCBDDDxxAAxBxDADDCBDBCCACCCCBBACDCDCCDxAxDCxxDxABBADDBADDxxAxDCAxDBBxxDDACxDDCAAAxCDBxxBDBBCCDBDDCBABDBACxDDxADADBxBDABAADBCDACBADxBxDDCCDCCADBBDCDABAxACCxCCCxADDBABADACDCxBBxCBAxDAxCxCxDxBxCAADCxxBABDCxBxCBCADBxCACDBAAxDDDxAxDABADBxDCCxDADADDxCCxxAABBACBDCACxADBACADxBxBBBCBADDDABABBBDCCCxCDBDCAxBCDADACADCxxDDDBBDBxBCDxxCxxBBDCDAxxBDACxBDxCxDDDDADBBCBACxxBDADACABBxACCACDxBxBxABADCABDxACADBBCDDCDBDxACBAAxDDxABCBDDBBxBCDxCADxBDBxDCxCABDxAxACBDDACCDxBACBCCDAACDABBBACCxBCBxBxxCCxCAxDxBDxDDDxDCxDAxBxDDDAAAxBABDBADxDBADCADDDCDDDDAAxCBxCDAAxABBxAxABBCDBDABCAACCBADDDDxDBDCxDCDCDAABxCxDACCBBxAxBBCxDDxADDBxDxBBCDCDDAxAxDAxADCBBBDCxCCxxxxCBACACACCDxBCxxBBDxBCCxCAADBAxAACDxCBCDABDCxDxCCCDxCCxDDxDCACDBDBCDBDxCDBCABAADBABCxBBACDBCABxCxDDDAABDABBDDBDBCxCCxCxCBBxACxxxBCAxACxCADCCBCDCCADADBxBDAABAxAABAADABCDxDAxBDDACCBDDDCCBABDxCxxDAxACBxBCBCABBDCCABADAAxxBxACxADACACxADCDxAxDCAxBCABBxCCxxACDxxCDACDADBACxDCCCDADBAxCxABADDDxBxBCBABBDBCBxABABDCCxxCBCAAACAACDCCADDDBBAABxBADDDBBBADAxDCBxBxCxxACCDxBDBAxDADDCBBACCCBAABCDDCCBxxBDAADCxADABACxDxxCCADCDBBDCDAAAAxACxABBBCDDCCxBAxADBBBCDxDBADADCAADxCCAAxBDDxxDBBCDCADDxxAACABABCDCCxDxDDDxABCxBxDDCBAxDxxCDxAxCDDDBxABxDAAACxAxCCxDxDDABxADDCxDCCABBxDxACAxCBCDDADAABADCABDxBCDxxAxBxADABAxACAxCDACBBxBBBCBAxDxxBxxCADBxxDxAAxCDCDCBCDxDDDxDCxADACBxxACDCAACBAADCD"

p3 = sum(
    d[p0] + d[p1] + d[p2] + (6 if x == 0 else 2 if x == 1 else 0)
    for p0, p1, p2 in zip(notes[::3], notes[1::3], notes[2::3])
    for x in [sum(n == "x" for n in (p0, p1, p2))]
)
print(p3)


# If using python3.12+ then you can use itertools.batched

p2 = sum(
    d[p0] + d[p1] + (2 if p0 != "x" and p1 != "x" else 0)
    for p0, p1 in batched(notes, 2)
)

p3 = sum(
    sum(d.get(n, 0) for n in batch) + (6 if x == 0 else 2 if x == 1 else 0)
    for batch in batched(notes, 3)
    for x in [batch.count("x")]
)

