import { expect } from 'chai';

kreyaGrpc.onResponse(response => {
  kreya.test('Should receive the expected result', () => {
    expect(response.content.success).to.be.true
  });
});

kreyaGrpc.onCallCompleted(call => {
  kreya.test('gRPC call should complete successfully', () => {
    expect(call.status.code).to.eql(0);
  });
});