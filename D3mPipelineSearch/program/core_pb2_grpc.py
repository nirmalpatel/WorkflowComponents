# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import core_pb2 as core__pb2


class CoreStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.CreatePipelines = channel.unary_stream(
        '/Core/CreatePipelines',
        request_serializer=core__pb2.PipelineCreateRequest.SerializeToString,
        response_deserializer=core__pb2.PipelineCreateResult.FromString,
        )
    self.ExecutePipeline = channel.unary_stream(
        '/Core/ExecutePipeline',
        request_serializer=core__pb2.PipelineExecuteRequest.SerializeToString,
        response_deserializer=core__pb2.PipelineExecuteResult.FromString,
        )
    self.ListPipelines = channel.unary_unary(
        '/Core/ListPipelines',
        request_serializer=core__pb2.PipelineListRequest.SerializeToString,
        response_deserializer=core__pb2.PipelineListResult.FromString,
        )
    self.DeletePipelines = channel.unary_unary(
        '/Core/DeletePipelines',
        request_serializer=core__pb2.PipelineDeleteRequest.SerializeToString,
        response_deserializer=core__pb2.PipelineListResult.FromString,
        )
    self.CancelPipelines = channel.unary_unary(
        '/Core/CancelPipelines',
        request_serializer=core__pb2.PipelineCancelRequest.SerializeToString,
        response_deserializer=core__pb2.PipelineListResult.FromString,
        )
    self.GetCreatePipelineResults = channel.unary_stream(
        '/Core/GetCreatePipelineResults',
        request_serializer=core__pb2.PipelineCreateResultsRequest.SerializeToString,
        response_deserializer=core__pb2.PipelineCreateResult.FromString,
        )
    self.GetExecutePipelineResults = channel.unary_stream(
        '/Core/GetExecutePipelineResults',
        request_serializer=core__pb2.PipelineExecuteResultsRequest.SerializeToString,
        response_deserializer=core__pb2.PipelineExecuteResult.FromString,
        )
    self.ExportPipeline = channel.unary_unary(
        '/Core/ExportPipeline',
        request_serializer=core__pb2.PipelineExportRequest.SerializeToString,
        response_deserializer=core__pb2.Response.FromString,
        )
    self.SetProblemDoc = channel.unary_unary(
        '/Core/SetProblemDoc',
        request_serializer=core__pb2.SetProblemDocRequest.SerializeToString,
        response_deserializer=core__pb2.Response.FromString,
        )
    self.StartSession = channel.unary_unary(
        '/Core/StartSession',
        request_serializer=core__pb2.SessionRequest.SerializeToString,
        response_deserializer=core__pb2.SessionResponse.FromString,
        )
    self.EndSession = channel.unary_unary(
        '/Core/EndSession',
        request_serializer=core__pb2.SessionContext.SerializeToString,
        response_deserializer=core__pb2.Response.FromString,
        )


class CoreServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def CreatePipelines(self, request, context):
    """Train step - multiple result messages returned via GRPC streaming.
    Request the TA2 system generate pipelines to satisfy a given task,
    training data, and targets.  The response is a stream of result messages
    indicating progress, failure, or completion of an individual pipeline
    creation task associated with the request.  The stream is closed by the
    server when all pipeline creation tasks have been completed.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ExecutePipeline(self, request, context):
    """Predict step - multiple results messages returned via GRPC streaming.
    Request the TA2 system execute a previously created pipeline against an
    input dataset.  This response is a stream of result messages indicating
    progress, failure, or completion of the pipeline execution task.  The
    stream is closed by the server when all pipeline execution tasks have
    been completed. Labels / predicted values are made available to TA3
    systems for user inspection.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListPipelines(self, request, context):
    """Lists all pipelines in session.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeletePipelines(self, request, context):
    """Deletes specified pipelines in session, returns IDs of successfully deleted pipelines. 
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CancelPipelines(self, request, context):
    """Cancels processing (creation or execution) of specified pipelines in session, but does not
    delete.  Returns IDs of successfully canceled pipelines.  State of a canceled pipeline is
    unspecified.  It could be useable or not.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetCreatePipelineResults(self, request, context):
    """Obtain results; lists existing pipelines then streams new results as they become available.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetExecutePipelineResults(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ExportPipeline(self, request, context):
    """Export executable of a pipeline, including any optional preprocessing used in session.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetProblemDoc(self, request, context):
    """Set problem schema for current session.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def StartSession(self, request, context):
    """Session management.
    Create a new user session, which provides a session context for creation and execution of pipelines.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def EndSession(self, request, context):
    """Terminate a user session and release associated context resources.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_CoreServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'CreatePipelines': grpc.unary_stream_rpc_method_handler(
          servicer.CreatePipelines,
          request_deserializer=core__pb2.PipelineCreateRequest.FromString,
          response_serializer=core__pb2.PipelineCreateResult.SerializeToString,
      ),
      'ExecutePipeline': grpc.unary_stream_rpc_method_handler(
          servicer.ExecutePipeline,
          request_deserializer=core__pb2.PipelineExecuteRequest.FromString,
          response_serializer=core__pb2.PipelineExecuteResult.SerializeToString,
      ),
      'ListPipelines': grpc.unary_unary_rpc_method_handler(
          servicer.ListPipelines,
          request_deserializer=core__pb2.PipelineListRequest.FromString,
          response_serializer=core__pb2.PipelineListResult.SerializeToString,
      ),
      'DeletePipelines': grpc.unary_unary_rpc_method_handler(
          servicer.DeletePipelines,
          request_deserializer=core__pb2.PipelineDeleteRequest.FromString,
          response_serializer=core__pb2.PipelineListResult.SerializeToString,
      ),
      'CancelPipelines': grpc.unary_unary_rpc_method_handler(
          servicer.CancelPipelines,
          request_deserializer=core__pb2.PipelineCancelRequest.FromString,
          response_serializer=core__pb2.PipelineListResult.SerializeToString,
      ),
      'GetCreatePipelineResults': grpc.unary_stream_rpc_method_handler(
          servicer.GetCreatePipelineResults,
          request_deserializer=core__pb2.PipelineCreateResultsRequest.FromString,
          response_serializer=core__pb2.PipelineCreateResult.SerializeToString,
      ),
      'GetExecutePipelineResults': grpc.unary_stream_rpc_method_handler(
          servicer.GetExecutePipelineResults,
          request_deserializer=core__pb2.PipelineExecuteResultsRequest.FromString,
          response_serializer=core__pb2.PipelineExecuteResult.SerializeToString,
      ),
      'ExportPipeline': grpc.unary_unary_rpc_method_handler(
          servicer.ExportPipeline,
          request_deserializer=core__pb2.PipelineExportRequest.FromString,
          response_serializer=core__pb2.Response.SerializeToString,
      ),
      'SetProblemDoc': grpc.unary_unary_rpc_method_handler(
          servicer.SetProblemDoc,
          request_deserializer=core__pb2.SetProblemDocRequest.FromString,
          response_serializer=core__pb2.Response.SerializeToString,
      ),
      'StartSession': grpc.unary_unary_rpc_method_handler(
          servicer.StartSession,
          request_deserializer=core__pb2.SessionRequest.FromString,
          response_serializer=core__pb2.SessionResponse.SerializeToString,
      ),
      'EndSession': grpc.unary_unary_rpc_method_handler(
          servicer.EndSession,
          request_deserializer=core__pb2.SessionContext.FromString,
          response_serializer=core__pb2.Response.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Core', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))