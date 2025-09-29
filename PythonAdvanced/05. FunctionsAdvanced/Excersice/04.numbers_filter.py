def even_odd_filter(**kwargs):
    for key, value in kwargs.items():
        if key=="even":
            kwargs[key] = [x for x in value if x%2==0]
        else:
            kwargs[key] = [x for x in value if x%2==1]
    return dict(sorted(kwargs.items(), key=lambda x: -len(x[1])))