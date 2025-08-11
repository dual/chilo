import { expect } from 'chai';

kreyaGrpc.onCallCompleted(call => {
  kreya.test('gRPC call should complete successfully', () => {
    expect(call.status.code).to.eql(0);
  });
});