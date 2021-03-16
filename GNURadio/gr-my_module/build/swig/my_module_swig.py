# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_my_module_swig')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_my_module_swig')
    _my_module_swig = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_my_module_swig', [dirname(__file__)])
        except ImportError:
            import _my_module_swig
            return _my_module_swig
        try:
            _mod = imp.load_module('_my_module_swig', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _my_module_swig = swig_import_helper()
    del swig_import_helper
else:
    import _my_module_swig
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        object.__setattr__(self, name, value)
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_method(set):
    def set_attr(self, name, value):
        if (name == "thisown"):
            return self.this.own(value)
        if hasattr(self, name) or (name == "this"):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add attributes to %s" % self)
    return set_attr



def high_res_timer_now():
    """high_res_timer_now() -> gr::high_res_timer_type"""
    return _my_module_swig.high_res_timer_now()

def high_res_timer_now_perfmon():
    """high_res_timer_now_perfmon() -> gr::high_res_timer_type"""
    return _my_module_swig.high_res_timer_now_perfmon()

def high_res_timer_tps():
    """high_res_timer_tps() -> gr::high_res_timer_type"""
    return _my_module_swig.high_res_timer_tps()

def high_res_timer_epoch():
    """high_res_timer_epoch() -> gr::high_res_timer_type"""
    return _my_module_swig.high_res_timer_epoch()
class cognitive(object):
    """
    <+description of block+>

    Constructor Specific Documentation:

    Return a shared_ptr to a new instance of my_module::cognitive.

    To avoid accidental use of raw pointers, my_module::cognitive's constructor is in a private implementation class. my_module::cognitive::make is the public interface for creating new instances.
    """

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def make():
        """
        make() -> cognitive_sptr

        <+description of block+>

        Constructor Specific Documentation:

        Return a shared_ptr to a new instance of my_module::cognitive.

        To avoid accidental use of raw pointers, my_module::cognitive's constructor is in a private implementation class. my_module::cognitive::make is the public interface for creating new instances.
        """
        return _my_module_swig.cognitive_make()

    make = staticmethod(make)
    __swig_destroy__ = _my_module_swig.delete_cognitive
    __del__ = lambda self: None
cognitive_swigregister = _my_module_swig.cognitive_swigregister
cognitive_swigregister(cognitive)

def cognitive_make():
    """
    cognitive_make() -> cognitive_sptr

    <+description of block+>

    Constructor Specific Documentation:

    Return a shared_ptr to a new instance of my_module::cognitive.

    To avoid accidental use of raw pointers, my_module::cognitive's constructor is in a private implementation class. my_module::cognitive::make is the public interface for creating new instances.
    """
    return _my_module_swig.cognitive_make()

class cognitive_sptr(object):
    """Proxy of C++ boost::shared_ptr<(gr::my_module::cognitive)> class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(boost::shared_ptr<(gr::my_module::cognitive)> self) -> cognitive_sptr
        __init__(boost::shared_ptr<(gr::my_module::cognitive)> self, cognitive p) -> cognitive_sptr
        """
        this = _my_module_swig.new_cognitive_sptr(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def __deref__(self):
        """__deref__(cognitive_sptr self) -> cognitive"""
        return _my_module_swig.cognitive_sptr___deref__(self)

    __swig_destroy__ = _my_module_swig.delete_cognitive_sptr
    __del__ = lambda self: None

    def make(self):
        """
        make(cognitive_sptr self) -> cognitive_sptr

        <+description of block+>

        Constructor Specific Documentation:

        Return a shared_ptr to a new instance of my_module::cognitive.

        To avoid accidental use of raw pointers, my_module::cognitive's constructor is in a private implementation class. my_module::cognitive::make is the public interface for creating new instances.
        """
        return _my_module_swig.cognitive_sptr_make(self)


    def history(self):
        """history(cognitive_sptr self) -> unsigned int"""
        return _my_module_swig.cognitive_sptr_history(self)


    def declare_sample_delay(self, *args):
        """
        declare_sample_delay(cognitive_sptr self, int which, int delay)
        declare_sample_delay(cognitive_sptr self, unsigned int delay)
        """
        return _my_module_swig.cognitive_sptr_declare_sample_delay(self, *args)


    def sample_delay(self, which):
        """sample_delay(cognitive_sptr self, int which) -> unsigned int"""
        return _my_module_swig.cognitive_sptr_sample_delay(self, which)


    def output_multiple(self):
        """output_multiple(cognitive_sptr self) -> int"""
        return _my_module_swig.cognitive_sptr_output_multiple(self)


    def relative_rate(self):
        """relative_rate(cognitive_sptr self) -> double"""
        return _my_module_swig.cognitive_sptr_relative_rate(self)


    def start(self):
        """start(cognitive_sptr self) -> bool"""
        return _my_module_swig.cognitive_sptr_start(self)


    def stop(self):
        """stop(cognitive_sptr self) -> bool"""
        return _my_module_swig.cognitive_sptr_stop(self)


    def nitems_read(self, which_input):
        """nitems_read(cognitive_sptr self, unsigned int which_input) -> uint64_t"""
        return _my_module_swig.cognitive_sptr_nitems_read(self, which_input)


    def nitems_written(self, which_output):
        """nitems_written(cognitive_sptr self, unsigned int which_output) -> uint64_t"""
        return _my_module_swig.cognitive_sptr_nitems_written(self, which_output)


    def max_noutput_items(self):
        """max_noutput_items(cognitive_sptr self) -> int"""
        return _my_module_swig.cognitive_sptr_max_noutput_items(self)


    def set_max_noutput_items(self, m):
        """set_max_noutput_items(cognitive_sptr self, int m)"""
        return _my_module_swig.cognitive_sptr_set_max_noutput_items(self, m)


    def unset_max_noutput_items(self):
        """unset_max_noutput_items(cognitive_sptr self)"""
        return _my_module_swig.cognitive_sptr_unset_max_noutput_items(self)


    def is_set_max_noutput_items(self):
        """is_set_max_noutput_items(cognitive_sptr self) -> bool"""
        return _my_module_swig.cognitive_sptr_is_set_max_noutput_items(self)


    def set_min_noutput_items(self, m):
        """set_min_noutput_items(cognitive_sptr self, int m)"""
        return _my_module_swig.cognitive_sptr_set_min_noutput_items(self, m)


    def min_noutput_items(self):
        """min_noutput_items(cognitive_sptr self) -> int"""
        return _my_module_swig.cognitive_sptr_min_noutput_items(self)


    def max_output_buffer(self, i):
        """max_output_buffer(cognitive_sptr self, int i) -> long"""
        return _my_module_swig.cognitive_sptr_max_output_buffer(self, i)


    def set_max_output_buffer(self, *args):
        """
        set_max_output_buffer(cognitive_sptr self, long max_output_buffer)
        set_max_output_buffer(cognitive_sptr self, int port, long max_output_buffer)
        """
        return _my_module_swig.cognitive_sptr_set_max_output_buffer(self, *args)


    def min_output_buffer(self, i):
        """min_output_buffer(cognitive_sptr self, int i) -> long"""
        return _my_module_swig.cognitive_sptr_min_output_buffer(self, i)


    def set_min_output_buffer(self, *args):
        """
        set_min_output_buffer(cognitive_sptr self, long min_output_buffer)
        set_min_output_buffer(cognitive_sptr self, int port, long min_output_buffer)
        """
        return _my_module_swig.cognitive_sptr_set_min_output_buffer(self, *args)


    def pc_noutput_items(self):
        """pc_noutput_items(cognitive_sptr self) -> float"""
        return _my_module_swig.cognitive_sptr_pc_noutput_items(self)


    def pc_noutput_items_avg(self):
        """pc_noutput_items_avg(cognitive_sptr self) -> float"""
        return _my_module_swig.cognitive_sptr_pc_noutput_items_avg(self)


    def pc_noutput_items_var(self):
        """pc_noutput_items_var(cognitive_sptr self) -> float"""
        return _my_module_swig.cognitive_sptr_pc_noutput_items_var(self)


    def pc_nproduced(self):
        """pc_nproduced(cognitive_sptr self) -> float"""
        return _my_module_swig.cognitive_sptr_pc_nproduced(self)


    def pc_nproduced_avg(self):
        """pc_nproduced_avg(cognitive_sptr self) -> float"""
        return _my_module_swig.cognitive_sptr_pc_nproduced_avg(self)


    def pc_nproduced_var(self):
        """pc_nproduced_var(cognitive_sptr self) -> float"""
        return _my_module_swig.cognitive_sptr_pc_nproduced_var(self)


    def pc_input_buffers_full(self, *args):
        """
        pc_input_buffers_full(cognitive_sptr self, int which) -> float
        pc_input_buffers_full(cognitive_sptr self) -> pmt_vector_float
        """
        return _my_module_swig.cognitive_sptr_pc_input_buffers_full(self, *args)


    def pc_input_buffers_full_avg(self, *args):
        """
        pc_input_buffers_full_avg(cognitive_sptr self, int which) -> float
        pc_input_buffers_full_avg(cognitive_sptr self) -> pmt_vector_float
        """
        return _my_module_swig.cognitive_sptr_pc_input_buffers_full_avg(self, *args)


    def pc_input_buffers_full_var(self, *args):
        """
        pc_input_buffers_full_var(cognitive_sptr self, int which) -> float
        pc_input_buffers_full_var(cognitive_sptr self) -> pmt_vector_float
        """
        return _my_module_swig.cognitive_sptr_pc_input_buffers_full_var(self, *args)


    def pc_output_buffers_full(self, *args):
        """
        pc_output_buffers_full(cognitive_sptr self, int which) -> float
        pc_output_buffers_full(cognitive_sptr self) -> pmt_vector_float
        """
        return _my_module_swig.cognitive_sptr_pc_output_buffers_full(self, *args)


    def pc_output_buffers_full_avg(self, *args):
        """
        pc_output_buffers_full_avg(cognitive_sptr self, int which) -> float
        pc_output_buffers_full_avg(cognitive_sptr self) -> pmt_vector_float
        """
        return _my_module_swig.cognitive_sptr_pc_output_buffers_full_avg(self, *args)


    def pc_output_buffers_full_var(self, *args):
        """
        pc_output_buffers_full_var(cognitive_sptr self, int which) -> float
        pc_output_buffers_full_var(cognitive_sptr self) -> pmt_vector_float
        """
        return _my_module_swig.cognitive_sptr_pc_output_buffers_full_var(self, *args)


    def pc_work_time(self):
        """pc_work_time(cognitive_sptr self) -> float"""
        return _my_module_swig.cognitive_sptr_pc_work_time(self)


    def pc_work_time_avg(self):
        """pc_work_time_avg(cognitive_sptr self) -> float"""
        return _my_module_swig.cognitive_sptr_pc_work_time_avg(self)


    def pc_work_time_var(self):
        """pc_work_time_var(cognitive_sptr self) -> float"""
        return _my_module_swig.cognitive_sptr_pc_work_time_var(self)


    def pc_work_time_total(self):
        """pc_work_time_total(cognitive_sptr self) -> float"""
        return _my_module_swig.cognitive_sptr_pc_work_time_total(self)


    def pc_throughput_avg(self):
        """pc_throughput_avg(cognitive_sptr self) -> float"""
        return _my_module_swig.cognitive_sptr_pc_throughput_avg(self)


    def set_processor_affinity(self, mask):
        """set_processor_affinity(cognitive_sptr self, std::vector< int,std::allocator< int > > const & mask)"""
        return _my_module_swig.cognitive_sptr_set_processor_affinity(self, mask)


    def unset_processor_affinity(self):
        """unset_processor_affinity(cognitive_sptr self)"""
        return _my_module_swig.cognitive_sptr_unset_processor_affinity(self)


    def processor_affinity(self):
        """processor_affinity(cognitive_sptr self) -> std::vector< int,std::allocator< int > >"""
        return _my_module_swig.cognitive_sptr_processor_affinity(self)


    def active_thread_priority(self):
        """active_thread_priority(cognitive_sptr self) -> int"""
        return _my_module_swig.cognitive_sptr_active_thread_priority(self)


    def thread_priority(self):
        """thread_priority(cognitive_sptr self) -> int"""
        return _my_module_swig.cognitive_sptr_thread_priority(self)


    def set_thread_priority(self, priority):
        """set_thread_priority(cognitive_sptr self, int priority) -> int"""
        return _my_module_swig.cognitive_sptr_set_thread_priority(self, priority)


    def name(self):
        """name(cognitive_sptr self) -> std::string"""
        return _my_module_swig.cognitive_sptr_name(self)


    def symbol_name(self):
        """symbol_name(cognitive_sptr self) -> std::string"""
        return _my_module_swig.cognitive_sptr_symbol_name(self)


    def input_signature(self):
        """input_signature(cognitive_sptr self) -> io_signature_sptr"""
        return _my_module_swig.cognitive_sptr_input_signature(self)


    def output_signature(self):
        """output_signature(cognitive_sptr self) -> io_signature_sptr"""
        return _my_module_swig.cognitive_sptr_output_signature(self)


    def unique_id(self):
        """unique_id(cognitive_sptr self) -> long"""
        return _my_module_swig.cognitive_sptr_unique_id(self)


    def to_basic_block(self):
        """to_basic_block(cognitive_sptr self) -> basic_block_sptr"""
        return _my_module_swig.cognitive_sptr_to_basic_block(self)


    def check_topology(self, ninputs, noutputs):
        """check_topology(cognitive_sptr self, int ninputs, int noutputs) -> bool"""
        return _my_module_swig.cognitive_sptr_check_topology(self, ninputs, noutputs)


    def alias(self):
        """alias(cognitive_sptr self) -> std::string"""
        return _my_module_swig.cognitive_sptr_alias(self)


    def set_block_alias(self, name):
        """set_block_alias(cognitive_sptr self, std::string name)"""
        return _my_module_swig.cognitive_sptr_set_block_alias(self, name)


    def _post(self, which_port, msg):
        """_post(cognitive_sptr self, swig_int_ptr which_port, swig_int_ptr msg)"""
        return _my_module_swig.cognitive_sptr__post(self, which_port, msg)


    def message_ports_in(self):
        """message_ports_in(cognitive_sptr self) -> swig_int_ptr"""
        return _my_module_swig.cognitive_sptr_message_ports_in(self)


    def message_ports_out(self):
        """message_ports_out(cognitive_sptr self) -> swig_int_ptr"""
        return _my_module_swig.cognitive_sptr_message_ports_out(self)


    def message_subscribers(self, which_port):
        """message_subscribers(cognitive_sptr self, swig_int_ptr which_port) -> swig_int_ptr"""
        return _my_module_swig.cognitive_sptr_message_subscribers(self, which_port)

cognitive_sptr_swigregister = _my_module_swig.cognitive_sptr_swigregister
cognitive_sptr_swigregister(cognitive_sptr)


cognitive_sptr.__repr__ = lambda self: "<gr_block %s (%d)>" % (self.name(), self.unique_id())
cognitive = cognitive.make;



