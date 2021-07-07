from typing import (
    Union, Optional, Any, IO, Iterable, AnyStr, Dict, List, Tuple
)


class Client:
    """Client的简介描述

    更多关于Client的信息描述。
    此处为段落描述内容 ...

    :param object data: 可迭代对象或者IO对象的类型
    :param str param1:
        字符串参数说明
    :param (:obj:`str`, optional) param2:
        可选参数说明，类型可能是字符或者字典
    :param param3:
        可选参数说明， 任意类型
        段落说明...
    :argument int:
        不定参数说明
    :keyword str keyword1:
        关键字1说明
    :keyword float keyword2:
        关键字2说明
    :keyword bool keyword3: 关键字3说明

    See also
    --------
    参见内容在这里写

    Notes
    -----
    注解内容在这里写

    """

    info = [{'id': 1}], [{'active': True}]

    def __init__(
            self,
            data: Union[Iterable[AnyStr], IO[AnyStr]],
            param1: str,
            param2: Optional[Union[str, Dict[str, Any]]] = None,
            param3: Optional[Any] = None,
            *args: int,
            **kwargs: Any
            ):
        self.data = data
        self.param1 = param1
        self.param2 = param2
        self.param3 = param3
        self.args = args
        self.kwargs = kwargs

    @classmethod
    def get_client_info(cls) -> Tuple[List[Dict[str, int]], List[Dict[str, bool]]]:
        """函数功能介绍

        :returns:
            二元组返回值说明
        :rtype:
            tuple(list(dict(str, str), list(dict(str, str))

        Examples
        --------
        >>> Client.get_client_info()
        ([{'id': 1}], [{'active': True}])
        """
        return cls.info
