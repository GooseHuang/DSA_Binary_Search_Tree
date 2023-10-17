```python



    root = bst.root
    new_node = insert(11, root)
    update_chain_depth(new_node)

    root = bst.root
    new_node = insert(24, root)
    update_chain_depth(new_node)


    root = bst.root
    new_node = insert(27, root)
    update_chain_depth(new_node)


    root = bst.root
    new_node = insert(2, root)
    update_chain_depth(new_node)

    root = bst.root
    new_node = insert(3, root)
    update_chain_depth(new_node)


    root = bst.root
    new_node = insert(15, root)
    update_chain_depth(new_node)

    root = bst.root
    new_node = insert(29, root)
    update_chain_depth(new_node)

    root = bst.root
    new_node = insert(37, root)
    update_chain_depth(new_node)

    root = bst.root
    new_node = insert(0, root)
    update_chain_depth(new_node)

    root = bst.root
    new_node = insert(100, root)
    update_chain_depth(new_node)

    root = bst.root
    new_node = insert(55, root)
    update_chain_depth(new_node)

    root = bst.root
    new_node = insert(57, root)
    update_chain_depth(new_node)

    root = bst.root
    new_node = insert(18, root)
    update_chain_depth(new_node)

    root = bst.root
    new_node = insert(17, root)
    update_chain_depth(new_node)

    root = bst.root
    new_node = insert(81, root)
    update_chain_depth(new_node)

    root = bst.root
    new_node = insert(99, root)
    update_chain_depth(new_node)

    root = bst.root
    new_node = insert(-1, root)
    update_chain_depth(new_node)


    root = bst.root
    new_node = insert(-2, root)
    update_chain_depth(new_node)
















print_node(node)

print_node(center)
print_node(center.left)
print_node(center.right)


print_node(node)


node = center.left
node.value
node.left.value

node.value
Out[7]: 70
node.left.value
Out[8]: 70



    # bst = BinarySearchTree.BinarySearchTree([ 81, 77, 70, 12, 92, 39, 31,
    #                                           59, 11, 25, 58, 52, 38, 84,
    #                                           21, 79, 78, 18,])

    # node_string = """
    #                 20  72  77  91  2  33  48  30  71  40  17  50  44  86  11  47  43  82  39
    #               """
    node_string = """
                    177  877  421  438  865  770  78  34  543  664  225  178  855  900  605  534  927  186  242  796  258  657  271  816  624  547  550  571  288  476  916  806  863  182  603  621  485  443  521  369  467  397  181  129  706  662  818  727  564  7  428  162  299  206  577  925  953  453  116  118  886  402  890  283  992  557  337  488  959  98  630  255  298  899  942  87  47  858  311  126  441  716  739  93  632  331  936  168  866  458  33  144  973  478  518  83  745  51  596  327  540  751  300  252  8  802  508  996  442  236  830  230  874  999  35  901  110  354  41  651  205  724  91  92  239  336  979  908  748  878  532  355  279  852  871  994  222  957  759  946  920  974  146  287  124  211  981  281  419  84  573  935  130  30  457  333  966  873  766  170  176  201  861  175  97  123  188  723  980  823  363  627  412  484  420  676  840  282  361  591  238  439  514  212  261  14  180  674  849  688  910  602  447  171  234  99  641  127  847  101  834  967  814  758  932  468  307  560  21  18  426  456  854  120  659  883  437  965  179  382  856  483  423  276  246  157  156  109  393  645  694  491  88  538  687  185  448  754  395  660  610  56  147  729  224  693  831  870  805  629  656  85  365  134  319  710  768  663  850  583  312  882  195  978  592  539  655  887  55  512  20  609  961  137  53  76  931  424  463  675  678  636  108  995  387  827  523  752  986  586  26  328  391  256  828  396  253  929  801  339  290  611  24  207  434  303  572  757  501  343  158  671  104  612  701  619  272  810  418  308  561  647  902  568  590  356  227  615  585  152  777  1  574  987  526  266  364  385  941  416  939  912  563  894  820  719  740  792  559  285  486  764  174  787  794  345  705  151  511  46  79  720  461  445  324  905  81  29  169  265  530  531  524  928  819  59  353  1000  991  359  254  637  891  121  16  37  789  788  71  780  427  594  717  496  431  301  472
                  """
    node_string = """
                    177  877  421  438  865  770  78  34  543  664  225  178  855  900  605  534  927  186  242  796  258  657  271  816  624  547  550  571  288  476  916  806  863  182  603  621  485  443  521  369  467  397  181  129  706  
                  
                  """
    
    
    
    # Good
    node_string = """
                    177  877   865  770  78  34  543  664  225  178   900  605  927  186  242  796  258  657  271   624  547  550  571  288  476  916  806  863  182  603  621  485  443  521  369  467   181  129  706  662   727  564  7  428  162   206  577  925  953  453  116  118  886  402  890   283  
                  """

    # Bad
    node_string = """
                    177  877   865  770  78  34  543  664  225  178   900  605  927  186  242  796  258  657  271   624  547  550  571  288  476  916  806  863  182  603  621  485  443  521  369  467   181  129  706  662   727  564  7  428  162   206  577  925  953  453  116  118  886  402  890  
                  """

    
    



```



## Records

```python

79  
70  84  
18  78  81  92  
11  39  77  
12  31  59  
25  38  58  
21  52  



78  
59  84  
21  77  81  92  
12  39  70  79  
11  18  31  58  
25  38  52  


77  
58  81  
21  70  79  92  
12  39  59  78  84  
11  18  31  52  
25  38  


70  
52  81  
21  59  79  92  
12  39  58  78  84  
11  18  31  77  
25  38  


70  
39  81  
21  58  79  92  
12  31  52  59  78  84  
11  18  25  38  77  



70  
39  81  
21  58  78  92  
12  31  52  59  77  79  84  
11  18  25  38  


get min depth?

70  
38  79  
21  58  78  84  
12  31  52  59  77  81  92  
11  18  25  39  
```

