import lambdata_Eric_Ramon.df_utils as dfu
import pandas as pd

# def test_train_val_test_split():
#     test_data = np.arange(10).reshape(10,1)
#     test_df = pd.DataFrame(test_data)
#     assert dfu.train_val_test_split(test_df) = Xtrt, ytrt, Xvt,
#                                                 yvt, Xtet, ytet

def test_null_check():
    test_data = {1:[1,None],
                 2:[None,1]
                }

    test_df = pd.DataFrame(test_data, columns = [1,2])
    assert dfu.null_check(test_df) == 2
