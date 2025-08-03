import { expect } from 'chai';

kreyaGrpc.onResponse(response => {
  kreya.test('Should receive the expected result', () => {
    expect(response.content.results).to.exist
  });
});