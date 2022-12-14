# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_util.ipynb.

# %% auto 0
__all__ = ['procrustes']

# %% ../nbs/00_util.ipynb 5
def procrustes(x:str, # input string
               appropriate_length:int=50, # desired length
               pad_with:str=" ", # character to pad with
               side:str="right" # which side to pad on ("left", "right")
              )->str: # string with desired length
    "A function to regulate string length."
    if len(x) > appropriate_length:
        return x[:appropriate_length]
    if len(x) < appropriate_length:
        to_pad = appropriate_length - len(x)
        pad = "".join([pad_with] * to_pad)
        if side == "right":
            x = x + pad
        elif side == "left":
            x = pad + x
        else:
            print("Invalid side argument; returning string as-is.")
    return x
